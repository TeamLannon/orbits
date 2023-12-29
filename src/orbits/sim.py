import math
import numpy as np
from astropy import units as u
from astropy import constants as const

class SimRun:
    """ Encapsulates all of the information for one run of a gravitational
        simulation
    """
    
    # The data type used for the object records
    datatype = np.dtype([('p',float, (3,)),
                         ('v',float, (3,)),
                         ('t',float)])    

    def __init__(self, dt, maxtime,
                 len_unit = u.meter, time_unit = u.second,
                 mass_unit=u.kilogram):
        """Construct a simulation run for a particular time "maxtime" broken
           into time steps of length "dt".  Change the default units with
           optional parameters.  Specify dt and maxtime as
           astropy.units.Quantity objects.
        """
        self.dt = dt.to(time_unit)
        # Allow one extra time step to store the initial values
        # math.ceil is to handle the case where dt doesn't divide
        # evenly into maxtime
        self.n_steps = math.ceil(maxtime.to(time_unit).value/self.dt.value) + 1
        # In the case that the given "maxtime" doesn't divide evenly by "dt,"
        # set the actual maxtime of this simulation to the end time
        self.maxtime = dt*(self.n_steps-1)
        self.objects = []
        self.len_unit = len_unit
        self.time_unit = time_unit
        self.mass_unit = mass_unit

    def add_object(self, name, x0, y0, z0, vx0, vy0, vz0, m, r):
        """Add one object to the simulation.  Call this for all
           objects before calling "run()"
        """
        # This is a numpy record array to hold the (x,y,z,vx,vy,vz,t)
        # values of the objects trajectory.
        # The array is long enough to hold all the values that will be
        # claculated during this simulation.
        pvt = u.Quantity(np.zeros(self.n_steps,
                                  dtype=SimRun.datatype),
                         u.StructuredUnit((self.len_unit,
                                           self.len_unit/self.time_unit,
                                           self.time_unit)))
        # Initialize the first position, velocity, and time entry
        # to the initial value and t = 0
        pvt[0]['p'][0]=x0.to(self.len_unit)
        pvt[0]['p'][1]=y0.to(self.len_unit)
        pvt[0]['p'][2]=z0.to(self.len_unit)
        pvt[0]['v'][0]=vx0.to(self.len_unit/self.time_unit)
        pvt[0]['v'][1]=vy0.to(self.len_unit/self.time_unit)
        pvt[0]['v'][2]=vz0.to(self.len_unit/self.time_unit)
        pvt[0]['t'] = 0*self.time_unit
        # Add the object to the list for later usage
        self.objects.append({"name":name,
                             "mass":m.to(self.mass_unit),
                             "radius":r.to(self.len_unit),
                             "pvt":pvt})

    def run(self):
        """Runs all the time steps in the simulation."""
        # Since t index = 0 is the initial condition, start by calculating
        # index = 1
        for i in range(1,self.n_steps):

            # Consider each object in the simulation
            for obj in self.objects:
                # Step 1: Calculate the acceleration caused by the gravitational
                # force from each other object in the simulation
                ax = 0*self.len_unit/(self.time_unit**2)
                ay = 0*self.len_unit/(self.time_unit**2)
                az = 0*self.len_unit/(self.time_unit**2)
                for src in self.objects:
                    if obj == src:
                        # Skip the same object
                        continue

                    # Do the acceleration calculation for this source
                    # and add it to the acceleration vector
                    ax += 0 # Replace with actual calculation
                    ay += 0 # Replace with actual calculation
                    az += 0 # Replace with actual calculation

                # Step 2: Update x, y, and z with vx, vy, vz
                obj['pvt'][i]['p'] += 0 # Replace with actual calculation

                # Step 3: Update vx, vy, and vz with ax, ay, and az
                obj['pvt'][i]['v'] += 0 # Replace with actual calculation

                # Step 4: Record the current time
                obj['pvt'][i]['t'] = self.dt*i
        

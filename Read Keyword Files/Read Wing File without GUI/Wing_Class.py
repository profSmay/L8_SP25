#region imports
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#endregion

#region class definitions
class Wing:

    def __init__(self):
        '''
        Constructor for the Wing class.  This class is used to store information about a wing
        and to process WingData.
        '''
        self.title = None
        self.dist_unit = None
        self.force_unit = None
        self.St = None
        self.Ss =  None
        self.modulus = None
        self.length = None
        self.taper = None
        self.load_factor = None
        self.margin = None
        self.sparH = None
        self.sparW = None
        self.up_dist = []
        self.aft_dist = []
        self.up_point = []
        self.aft_point = []

    def processWingData(self,data):
        '''
        Reads the array of data, parses each line and looks for information.
        The file must be in the expected format.
        :param data: An array of strings with format: name, value(s)
        :return: nothing
        '''
        #from the array of strings, fill the wing data
        for line in data: #loop over all the lines
            # replace leading whitespace, quotes and parentheses
            line = line.strip().replace("'","").replace('"','').replace("(","").replace(")","")
            line=line.replace(', ', ',') # remove internal whitespaces after a comma.
            #split the line at commas
            cells=line.split(',')
            
            # convert everything to lowercase
            keyword=cells[0].lower()
    
            # region process line based on keyword using match-case structure
            # process the single data item keywords
            match keyword:
                case 'title':
                    self.title=cells[1]
                case 'distance_unit':
                    self.dist_unit=cells[1]
                case 'force_unit':
                    self.force_unit=cells[1]
                case 'tensile_strength':
                    self.St=float(cells[1])
                case 'shear_strength':
                    self.Ss=float(cells[1])
                case 'modulus':
                    self.modulus=float(cells[1])
                case 'wing_length':
                    self.length=float(cells[1])
                case 'wing_taper':
                    self.taper=float(cells[1])
                case 'load_factor':
                    self.load_factor=float(cells[1])
                case 'margin_of_safety':
                    self.margin=float(cells[1])
                case 'spar_envelope':
                    self.sparH=float(cells[1])
                    self.sparW=float(cells[2])
                # process the INDEFINITE NUMBER OF ITEMS keywords
                case 'dist_up_load':
                    this_load=[cells[1]]
                    for cell in cells[2:]:
                        value=float(cell)
                        this_load.append(value)
                    self.up_dist.append(this_load)
                case 'dist_aft_load':
                    this_load=[cells[1]]
                    for cell in cells[2:]:
                        value=float(cell)
                        this_load.append(value)
                    self.aft_dist.append(this_load)
                case 'point_up_load':
                    this_load=[cells[1]]
                    for cell in cells[2:]:
                        value=float(cell)
                        this_load.append(value)
                    self.up_point.append(this_load)
                case 'point_aft_load':
                    this_load=[cells[1]]
                    for cell in cells[2:]:
                        value=float(cell)
                        this_load.append(value)
                    self.aft_point.append(this_load)
                #endregion

    def generate_report(self):
        '''
        Produces a nicely formatted string for display on CLI or GUI
        :return: A formatted, multiline string
        '''
        report = '\tTitle: '+ self.title
        report += '\n\tWing length: '+ str(self.length)
        report += '\n\tLoad factor: '+ str(self.load_factor)

        report +='\n\n'
        report += '\n\t\t Distributed Loads - Upwards'

        for set in self.up_dist:
            report += '\n\nLoad Set: ' + set[0]
            for i in range(1,len(set),2):
                report += '\n' + str(set[i]) + "   " + str(set[i+1])

        return report
#endregion
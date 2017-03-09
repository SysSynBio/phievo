""" 
This file provide the basic template to define new interactions.
You may want first to search/replace Dummy_Interaction by a more adapted name.

For reminder, the algorithm will use this file as follow:
When affecting new mutations, it use the number_Dummy_Interaction() method to know the number of possible interactions.
If this interaction is chosen, mutation.random_Interaction() will call the random_Dummy_Interaction() method defined below.
If this kind of interaction is deleted, mutation.remove_Interaction(), through classes_eds2.clean_Nodes() needs the outputs_to_delete() method defined below.
Finally, when integrating the equation, the C-code is generated by the Dummy_Interaction_deriv_inC() method defined below.

Note also that, along with this file, you have to modify the following modules to make your interaction available:
Networks/interaction.py (which import the interaction in the main program)
Networks/pretty_graph2.py (only for display... but it may be useful)
your initialization.py file
"""
print("Execute InteractionTemplate.py (Interaction Template)")

import classes_eds2
import mutation
import copy
import deriv2

##### Main class definition #####

# First defining default ranges for parameters.
# These are typically copy pasted in the 'initialization' file where they can be customized for each run.
mutation.dictionary_ranges['Dummy_Interaction.parameter1']= Some function of mutation.C, mutation.T, mutation.L
mutation.dictionary_ranges['Dummy_Interaction.parameter2']= Some function of mutation.C, mutation.T, mutation.L

class Dummy_Interaction(classes_eds2.Interaction):
    """ A Dummy_Interaction """
    
    def __init__(self,a=0,d=0):
        """Initialize all the parameters and the allowed structure of the interaction (input and output)"""
        classes_eds2.Node.__init__(self)
        self.parameter1=a
        self.parameter2=d
        self.label='Dummy_Interaction'
        # the input and ouput attributes are used by classes_eds2.check_grammar()
        # Typical values are 'Species', 'Degradable' or 'TModule'
        self.input=[#<'One Tag or TModule per input '>#]
        self.output=[#<'One Tag or TModule per input '>#]
    
    def outputs_to_delete(self,net):
        """ Returns the objects to delete when removing the Dummy_Interaction, typically some of the outputs of the interaction or nothing"""
        return [] #by default
        return net.graph.successors(self) #use this one when the interaction create a new species (PPI, LR or Phospho typically)

##### Attributes attached to the Network Class #####

def new_Dummy_Interaction(self,Input1, Input2,parameter1,parameter2,output_parameters):
    """Create a new Dummy_Interaction and its Outputs if necessary and add them to self (Network), should return a list of the interaction and the species created"""
    output = classes_eds2.Species(output_parameters)
    interaction = Dummy_Interaction(parameter1,parameter2)
    if interaction.check_grammar([Input1,Input2], [output]):
        self.add_Node(output)
        self.add_Node(interaction)
        self.graph.add_edge(Input1,interaction)
        self.graph.add_edge(Input2,interaction)
        self.graph.add_edge(interaction,output)
        return [interaction,output]
    else:
        print "Error in grammar in creation of new_Dummy_Interaction "
        return None

def check_existing_Dummy_Interaction(self,Input1, Input2):
    """Check if a Dummy_Interaction exists between the given Inputs, used to avoid to create already existing interaction"""
    if self.list_types.has_key('Dummy_Interaction'): #goes through the list of interactions
        for reaction in self.list_types['Dummy_Interaction']:
            if #<test here if the reaction you want to create correspond to this one>#:
                return True
    return False

def list_possible_Dummy_Interaction(self):
    """Return the list of all possible new Dummy_Interactions"""
    list_possible = []
    #<Insert here some method to create the list of possible new Dummy_Interactions>#
    return list_possible

def number_Dummy_Interaction(self):
    """ Computes the number of possible new Dummy_Interactions, used when the algorithm determine the next mutation"""
    return len(self.list_possible_Dummy_Interaction()) #by default but you may want to optimize

### Now we attach those attributes to the Network Class ###
setattr(classes_eds2.Network,'new_Dummy_Interaction',new_Dummy_Interaction)
setattr(classes_eds2.Network,'check_existing_Dummy_Interaction',check_existing_Dummy_Interaction)
setattr(classes_eds2.Network,'list_possible_Dummy_Interaction',list_possible_Dummy_Interaction)
setattr(classes_eds2.Network,'number_Dummy_Interaction',number_Dummy_Interaction)

##### Attributes attached to the Mutable_Network Class #####

def new_random_Dummy_Interaction(self, Input1, Input2):
    """Creates a new Dummy_Interaction with random parameters and output types by calling the new_Dummy_Interaction() method"""
    # Generate random parameters
    a = mutation.sample_dictionary_ranges('Dummy_Interaction.parameter1',self.Random)
    d = mutation.sample_dictionary_ranges('Dummy_Interaction.parameter2',self.Random)
    return self.new_Dummy_Interaction(Input1,Input2,a,d,output_parameters)

def random_Dummy_Interaction(self):
    """Creates a new random Dummy_Interaction among all possible ones by calling the new_random_Dummy_Interaction() method"""
    if self.list_types.has_key('key allowing this type of interaction'):
        list_possible = self.list_possible_Dummy_Interaction()
        if list_possible:
            #create randomly one Dummy_Interaction among those possible
            [Input1,Input2] = self.Random.choice(list_possible)
            return self.new_random_Dummy_Interaction(Input1,Input2)
        else:
            print "In random_Dummy_Interaction : no other possible random_dummy_Interaction, Error"
            return None
    else:
        print "Error in random_Dummy_Interaction (try to create a Dummy_Interaction from non existing pieces)"
        return None

### Now we attach the attributes to the Mutable_Network Class ###
setattr(mutation.Mutable_Network,'random_Dummy_Interaction',random_Dummy_Interaction)
setattr(mutation.Mutable_Network,'new_random_Dummy_Interaction',new_random_Dummy_Interaction)

###########Integration C Tools ##################

def Dummy_Interaction_deriv_inC(net):
    """Return a string of C-code describing the equation for all the Dummy_Interactions in net"""
    func="\n/**************Dummy_Interaction interactions*****************/\n"
    # Loop over all Dummy_Interaction if there is at least one
    if net.list_types.has_key('Dummy_Interaction'):
        for index in net.list_types['Dummy_Interaction']:
            Output = net.graph.successors(index) #finds the Outputs
            [Input1,Input2] = net.graph.predecessors(index) #find the Inputs
            
            # defines interaction rate, input_id_list will decreases and output_id_list increases at rate rate1
            rate1 = String combining Input1.id, Input2.id, parameter1, parameter2
            func += deriv2.compute_leap([input_id_list],[output_id_list],rate1) 
            
            rate2 = String combining Input1.id, Input2.id, parameter1, parameter2
            func += deriv2.compute_leap([input_id_list],[output_id_list],rate2)
    else:
        func += "No Dummy_Interaction in this network\n"
    return func
    
##### Update of the deriv2 method #####
deriv2.Dummy_Interaction_deriv_inC = Dummy_Interaction_deriv_inC

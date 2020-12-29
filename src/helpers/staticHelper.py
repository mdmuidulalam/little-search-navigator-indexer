# This file should not be changed if not absolutely necessary

''' 
Problem of changing this file is it can break the whole application as
many files directly depends on it.

Treat this file as library. We always need to maintain backward compatibility.
'''
class StaticHelper():

    @staticmethod
    def isInterfaceResloved(instance, interface):
        if not isinstance(instance, interface): 
            raise Exception('Bad interface')

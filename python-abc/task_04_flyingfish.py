#!/usr/bin/env python3
'''4. The Enigmatic FlyingFish - Exploring Multiple Inheritance'''


class Fish:
    '''Class Fish'''
    def __init__(self):
        '''Initialization of the Fish class'''
        pass

    def swim(self):
        '''Method swim'''
        print("The flying fish is swimming")

    def habitat(self):
        '''Method habitat'''
        print("The fish lives in water")


class Bird:
    '''Class Bird'''
    def __init__(self):
        '''Initialization of the Bird class'''
        pass

    def fly(self):
        '''Method fly'''
        print("The bird is flying")

    def habitat(self):
        '''Method habitat'''
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''Class FlyingFish inherits from Fish and Bird'''
    def __init__(self):
        '''Initialization of the FlyingFish class'''
        pass

    def swim(self):
        '''Method swim'''
        print("The flying fish is swimming!")

    def fly(self):
        '''Method fly'''
        print("The flying fish is soaring!")

    def habitat(self):
        '''Method habitat'''
        print("The flying fish lives both in water and the sky!")

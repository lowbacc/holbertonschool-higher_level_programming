#!/usr/bin/env python3
'''5. The Mystical Dragon - Mastering Mixins'''


class SwimMixin:
    '''Mixin class that provides swimming ability'''
    def swim(self):
        '''Method swim'''
        print("The creature swims!")


class FlyMixin:
    '''Mixin class that provides flying ability'''
    def fly(self):
        '''Method fly'''
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''Dragon class that uses both swimming and flying abilities from mixins'''
    def roar(self):
        '''Method roar'''
        print("The dragon roars!")

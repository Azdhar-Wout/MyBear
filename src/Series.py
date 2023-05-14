'''
Implémenter la classe Series dont le constructeur prend en paramètre une liste de valeurs comme données, et un nom sous forme de chaîne de caractères.
'''

class Series:
    
    def __init__(self, list_of_values, name):
        self.name = name
        self.list_of_values = list_of_values
        
        
    def __str__(self):
        return f"{self.name}[{self.list_of_values}]"
    
    
    '''
    @property
    def iloc(self) -> Any | Series
    '''
        
    
    def max(self):
        max_value = self.list_of_values[0]
        for i in range(len(self.list_of_values)):
            if self.list_of_values[i] > max_value:
                max_value = self.list_of_values[i]
        return max_value
    
    
    def min(self):
        min_value = self.list_of_values[0]
        for i in range(len(self.list_of_values)):
            if self.list_of_values[i] < min_value:
                min_value = self.list_of_values[i]
        return min_value
       
        
    def mean(self):
        qty = len(self.list_of_values)
        values_sum = 0
        for i in range(len(self.list_of_values)):
            values_sum += self.list_of_values[i]
        return values_sum/qty
        

    def std(self):
        pass
        
    
    def count(self):
        count = 0
        for i in range(len(self.list_of_values)):
            if self.list_of_values[i] is not None:
                count += 1
        return count
# comments & Docs
    

class Calc:
''' simple calculator class '''

    def sum(self,x,y): #BUG issue TODO
    '''
    function to sum 2 values , x , y
    x : int
    y : int
    return : int

    '''
        result = x+y
        return result


c = Calc()
print(c.sum(2,3))

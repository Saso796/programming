class kitchenapplianc:
    def on():
        pass
    def off():
        pass
    
class kitchenAppliancCanSetTemp(kitchenapplianc):
    def set_temp():
        pass
    
class oven(kitchenAppliancCanSetTemp):
    def on():
        return 'Im on'
    def off():
        return 'Im off'
    def set_temp():
        return 'Im 180'
    
class mixer(kitchenapplianc):
    def on():
        return 'Im on'
    def off():
        return 'Im off'
    
print(mixer.on())
print(oven.set_temp())

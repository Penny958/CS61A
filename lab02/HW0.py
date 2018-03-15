def yak(zebra):
    return 20 // zebra

def llama(alpaca):
    zebra = 0
    def yak(zebra):
        return alpaca(zebra)
    return yak

print(llama(yak)(4))
"""

Calculate the cost for a car to get cleaned at the car wash.

The car will be given in the form of a dict,
containing the properties of the car:
    type: sedan, suv, coupe, van, truck, sport
    brand: <any car brand>
    colour: <any colour>

The cleaning costs for cars is:
    sedan: $105
    suv: $180
    coupe: $98
    van: $222
    truck: $299
    sport: $315

black cars cost an extra $13
white cars cost an extra $20
pink cars are $69 cheaper
green cars get a 2% discount
variegated cars cost half the cleaning price

If the car is a sports car or a luxury car, an additional "special care"
charge of 50% is applied after cleaning.
Luxury cars are cars with the following brands:
    bmw, mercedes, audi, tesla, porsche, ferrari, lamborghini


Example 1:
    Input:  {"type": "sedan", "brand": "mitsubishi", "colour": "black"}
    Output: 118

Example 2:
    Input:  {"type": "sport", "brand": "audi", "colour": "white"}
    Output: 502.5


"""

def car_wash(car):
    # Your code goes here

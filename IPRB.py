# Project Roslalind: Mendel's First Law

'''
     y    y
  -----------
Y | Yy | Yy |
  |----------
y | Yy | yy |
  -----------

Input:
    k -> # YY
    m -> # Yy
    n -> # yy

Output: The probability that 2 random organisms will produces and individual with at least one Y.

Consider all possible outcomes and their likelihood...

Result    Prob of Result               Prob to produce Y
 kk      (k/tot)*((k-1)/(tot-1))              1.0
 km      (k/tot)*(m/(tot-1))                  1.0
 kn      (k/tot)*(n/(tot-1))                  1.0
 mk      (m/tot)*(k/(tot-1))                  1.0
 mm      (m/tot)*((m-1)/(tot-1))              0.75
 mn      (m/tot)*(n/(tot-1))                  0.5
 nk      (n/tot)*(k/(tot-1))                  1.0
 nm      (n/tot)*(m/(tot-1))                  0.5
 nn      (n/tot)*((n-1)/(tot-1))              0.0

 Answer = prob(kk) + prob(km) + prob(kn) + prob(mk) + 0.75*prob(mm) + 0.5*prob(mn) + 1.0*prob(nk) + 0.5*prob(nm)

'''

# Globals for convenience
populations = []
total = 0

def prob(index1, index2):
    '''
    Returns the probability of two organisms being chosen
    '''
    print("{0}, {1}, {2}".format(populations, index1, index2))
    if(index1 == index2):
        pop = populations[index1]
        prob = (pop / total) * ((pop-1) / (total-1))
    else:
        prob = (populations[index1] / total) * (populations[index2] / (total-1))
    return prob


def main():
    global populations, total # Must be explicit to write to global variables in Python
    with open('IPRB_dataset.txt', 'r') as df:
        populations = [int(number) for number in df.read().split()] # We want a list of numbers
    print(populations)

    total = sum(populations)
    answer = prob(0, 0) + prob(0, 1) + prob(0, 2) + \
             prob(1, 0) + 0.75*prob(1, 1) + 0.5*prob(1, 2) + \
             prob(2, 0) + 0.5*prob(2, 1) + 0.0*prob(2, 2)
    print(answer)


if __name__ == '__main__':
    main()


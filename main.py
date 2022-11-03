from model.fri import FRI
from model.field import FieldElement, Field
from model.polynomial import Polynomial
from model.proofstream import ProofStream

if __name__ == "__main__":
    """
    Reference: https://aszepieniec.github.io/stark-anatomy/basic-tools
    """
    
    # init filed
    field = Field.main()
    degree = 7 # d+1 will be power of 2

    # e.g. poly
    coeffiecients = [1,3,5,7,9, 11, 13]
    egpoly = Polynomial([FieldElement(i, field) for i in coeffiecients]) # f(x) = 1 + 3x + 5x^2 + 7x^3 + 9x^4 + 11x^5 + 13x^6

    # init parameters
    num_colinearity_tests = 2
    expansion_factor = 2
    initial_domain_length = 1<<(len(bin(degree+4*num_colinearity_tests)[2:])) * expansion_factor # 2^{log2(degree+4*num_colinearity_test)} * expansion_factor
    print(initial_domain_length)
    generator = field.generator()
    offset = generator
    omega = field.primitive_nth_root(initial_domain_length)
    
    # init fri
    fri = FRI(offset, omega, initial_domain_length, expansion_factor, num_colinearity_tests)

    fri_domain = fri.eval_domain()

    # evaluate polynomial to obtain codewords
    codewords = egpoly.evaluate_domain(fri_domain)
    print(len(codewords))

    # init proof stream 
    proof_stream = ProofStream()

    # prove
    indices = fri.prove(codewords, proof_stream)
    proof = proof_stream.serialize()

    print(indices)

    # init proof stream 
    proof_stream = ProofStream()
    proof_stream = proof_stream.deserialize(proof)
    polynomial_values = []
    verifier_accepts = fri.verify(proof_stream, polynomial_values)
    print(verifier_accepts)
    

    



    

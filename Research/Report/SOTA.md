# SOTA PSI methods

## Private Set Intersection: Are Garbled Circuits Better than Custom Protocols?

创新点：
- It explores the feasibility and efficiency of using generic garbled circuit methods to implement private set intersection (PSI), and compares them with previous custom protocols based on homomorphic encryption and other public-key techniques.
- It proposes three classes of protocols tailored to different set sizes and domains, all based on Yao's generic garbled-circuit method.
- It shows that using garbled circuit methods can directly perform more complex secure computations, such as adding a simple information-auditing mechanism to the PSI protocols.
- It implements the proposed protocols and evaluates them on typical desktop environments, showing that they can run on million-element sets and be competitive with the fastest custom protocols.

局限：
- It only considers the semi-honest security model, which assumes that parties follow the protocol but may try to learn additional information from the protocol execution. This model may not capture realistic adversarial behaviors, such as modifying software or deviating from the protocol. The paper does not provide any security guarantees or techniques for stronger security models, such as malicious or covert adversaries.
- It relies on the decisional Diffie-Hellman assumption and the random oracle model for the security of its protocols. These assumptions may not hold in some settings or may be subject to attacks by quantum computers. The paper does not explore alternative assumptions or models that may be more realistic or robust.
- It does not address some practical issues or challenges that may arise in real-world applications of PSI, such as handling dynamic sets, dealing with errors or noise in the input data, supporting multiple parties or queries, or optimizing communication and computation trade-offs. The paper does not compare its protocols with other solutions that may address these issues or challenges.

## Practical Private Set Intersection Protocols with Linear Computational and Bandwidth Complexity

创新点：
The paper proposes several protocols for private set intersection (PSI), which is a problem where two parties want to find the common elements in their sets without revealing anything else. The paper explores different variations of PSI, such as authorized PSI (APSI), where one party needs to have signatures from a trusted authority on its set elements, and PSI with data transfer (PSI-DT), where one or both parties have data associated with their set elements. The paper claims to improve the efficiency and security of existing PSI techniques, and presents protocols that have linear computational and bandwidth complexity. The paper also compares its protocols with prior work in terms of security model, adversary type, and performance.

局限：
Some possible limitations of the paper are:
- The paper assumes that the CA in APSI is honest and does not collude with the server or the client, which may not be realistic in some scenarios.
- The paper does not provide security proofs for malicious adversaries for the PSI and APSI protocols, leaving them as future work.
- The paper relies on the RSA assumption and the random oracle model for some of the protocols, which may not be the most efficient or secure choices.
- The paper does not consider other set operations besides intersection, such as union, difference, or cardinality.
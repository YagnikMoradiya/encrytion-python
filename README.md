# How to do encryption:

    # Hill Cifer:

        [1] Cifer Text = E(K,P) = P * K mod 26
        Here, E = Encryption
              K = Key
              P = Plain text in the matrix Form

        * Example (Using 3 * 3 Matrix): 
            (c1, c2, c3) = (p1, p2, p3)*(Key Matrix) mod 26

# How to do decryption

    # Hill Cifer:

        [1] Plain Text = D(K,C) = C * K(inverse) mod 26

            Here, D = Decryption
                  K = Key
                  C = Cifer text in the matrix Form
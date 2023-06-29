import string_histogram as sh
import frequencies as fq
import encode_text as enc


def crack_caesar(exampletext, text):
    vector_array = []
    E = fq.frequencies(sh.string_histogram(exampletext))

    O = []

    for char in range(0, 26):
        O.append(fq.frequencies(sh.string_histogram(enc.encode_text(text, -char))))
    print(len(O))
    for i in range(0, 26):
        chi_square = 0
        for j in range(0, 26):
            if E[j] == 0:
                chi_square += ((O[i][j] - E[j]) ** 2) / 1
            else:
                chi_square += ((O[i][j] - E[j]) ** 2) / E[j]
        vector_array.append(chi_square)

        min_vector = vector_array.index(min(vector_array))

        new_text = enc.encode_text(text, -min_vector)

    return new_text


extext = ("I know that virtue to be in you, Brutus, As well as I do know your outward favour. Well, " +
          "honour is the subject of my story. I cannot tell what you and other men Think of this life; but, " +
          "for my single self, I had as lief not be as live to be In awe of such a thing as I myself. I was " +
          "born free as Caesar; so were you: We both have fed as well, and we can both Endure the " +
          "winter's cold as well as he: For once, upon a raw and gusty day, The troubled Tiber chafing " +
          "with her shores, Caesar said to me 'Darest thou, Cassius, now Leap in with me into this " +
          "angry flood, And swim to yonder point?' Upon the word, Accoutred as I was, I plunged in " +
          "And bade him follow; so indeed he did. The torrent roar'd, and we did buffet it With lusty " +
          "sinews, throwing it aside And stemming it with hearts of controversy; But ere we could " +
          "arrive the point proposed, Caesar cried 'Help me, Cassius, or I sink!' I, as Aeneas, our great " +
          "ancestor, Did from the flames of Troy upon his shoulder The old Anchises bear, so from the " +
          "waves of Tiber Did I the tired Caesar. And this man Is now become a god, and Cassius is A " +
          "wretched creature and must bend his body, If Caesar carelessly but nod on him. He had a " +
          "fever when he was in Spain, And when the fit was on him, I did mark How he did shake: 'tis " +
          "true, this god did shake; His coward lips did from their colour fly, And that same eye whose " +
          "bend doth awe the world Did lose his lustre: I did hear him groan: Ay, and that tongue of his " +
          "that bade the Romans Mark him and write his speeches in their books, Alas, it cried 'Give me " +
          "some drink, Titinius,' As a sick girl. Ye gods, it doth amaze me A man of such a feeble temper " +
          "should So get the start of the majestic world And bear the palm alone.")
cotext = ("Reu jf zk zj. Wfi kyzj kzdv Z nzcc cvrmv pfl: Kf-dfiifn, zw pfl gcvrjv kf jgvrb nzky dv, Z nzcc " +
          "tfdv yfdv kf pfl; fi, zw pfl nzcc, Tfdv yfdv kf dv, reu Z nzcc nrzk wfi pfl.")
print(crack_caesar(extext, cotext))

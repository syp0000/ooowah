### input: ["abed", "Weff", "Wefewfv", "qqfac", "accewef"]
### output:  리스트에 있는 단어중 "a" 가 들어간 단어들만 넣은 리스트로 출
#력
def main(word):
    m = []
    for a in word:
        if 'a' in a:
            m.append(a)
    print(m)
    


if __name__== "__main__":
    lists = ["abed", "Weff", "Wefewfv", "qqfac", "accewef"]
    main(lists)

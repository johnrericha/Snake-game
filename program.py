from tinydb import TinyDB, Query

db = TinyDB("databaze.json")
query = Query()
def game():
    f = open("demofile.txt")
    print(f.read())
    
def registr():
    username = input("uzivatelske jmeno:")
    userpassword = input("uzivatelske heslo:")



    
    result = db.get(query.user == username)





    if result:
        print("uzivatelske jmeno existuje")
    elif len(userpassword) < 10:
        print("kratke heslo. Musi mit min 10 znaku")  
    else:
        
        db.insert({
        "user": username, 
        "password" : userpassword,
        
        })
        print("jste zaregistrovan")


def login():
    username = input("uzivatelske jmeno:")
    userpassword = input("uzivatelske heslo:")
    result = db.get(query.user == username)
    pw = result.get("password")
    if result:
        if pw == userpassword:
            print("Heslo a uzivatelske jmeno existuji jste prihlasen")
            game()
            
        else:
            print("uzivatelske heslo je spatne")
    else:
        print("uzivatelske jmeno neexistuje")

def main():
    print("1) login")
    print("2) registr")
    user = input()
    
    if user == "1":
        login()
    
    elif user == "2":
        registr()

if __name__ == "__main__":
    main()



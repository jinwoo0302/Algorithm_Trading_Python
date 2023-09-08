class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name=name
        self.phone_number=phone_number
        self.e_mail=e_mail
        self.addr=addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)


def set_contact():
    name=input("name: ")
    phone_number=input("phone_number: ")
    e_mail=input("e_mail: ")
    addr=input("addr: ")
    contact=Contact(name, phone_number, e_mail, addr)
    return contact

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu=input("메뉴선택: ")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name ==name:
            del contact_list[i]


def store_contact(contact_list):
    f=open("contact_db.txt","wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def load_contact(contact_list):
    f=open("contact_db.txt","rt")
    lines=f.readlines() #readlines()가 파일의 모든 데이터를 읽네.
    num=len(lines)/4
    num=int(num)

    for i in range(num):
        name=lines[4*i].rstrip('\n')
        phone=lines[4*i].rstrip('\n')
        email=lines[4*i].rstrip('\n')
        address=lines[4*i].rstrip('\n')
        contact=Contact(name, phone, email, address)
        contact_list.append(contact)
    f.close()

def run():
    contact_list=[]
    load_contact(contact_list)
    while 1:
        menu=print_menu() #print_menu()를 호출하고 그 결과를 menu변수에 할당
        if menu ==1:
            contact=set_contact()
            contact_list.append(contact)
        elif menu==2:
            print_contact(contact_list)
        elif menu==3:
            name = input("Name: ")
            delete_contact(contact_list,name)
        elif menu==4:
            store_contact(contact_list)
            break



if __name__=="__main__":
    run()
import pymysql

conn = None
cur = None

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',db='sqlDB', charset='utf8')

# 커서
cur = conn.cursor()

# userTBL의 회원 데이터 Insert
sql=""

# userID, name, birthYear, addr : NOT NULL
userID = ""
name = ""
birthYear = ""
addr = ""
mobile1 = ""
mobile2 = ""
height = ""

while (True) :
    userID = input("사용자 ID ==> ")
    if userID == "" :
        break
    name = input("사용자 이름 ==> ")
    if name == "" :
        break
    birthYear = input("사용자 출생년도 ==> ")
    if birthYear == "":
        break
    addr = input("사용자 주소 ==> ")
    if addr == "":
        break
    mobile1 = input("사용자 전화번호 앞 세자리 ==> ")
    if mobile1 == "":
        break
    mobile2 = input("사용자 전화번호 뒷 여덟자기 ==> ")
    if mobile2 == "":
        break
    height = input("사용자 키 ==> ")
    if height == "":
        break

    sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mobile1, mobile2, height, mDate ) VALUE" \
          "('"+userID+"' , '" + name + "' , " + birthYear + " , '" + addr + "', '" + mobile1 + "' , '" + mobile2 + "' ," + height + ", + CURDATE())"
    cur.execute(sql)

conn.commit()
conn.close()



############################################################
# (A) ANSWER START
class Data:
    def __init__(self,inputlist):
        self.data = inputlist
    def get(self):
        return self.data
class Filtered_Data(Data):
    def __init__(self,inputlist):
        self.data = inputlist
    def get_records(self):
        temp = self.data
        del temp[0]
        return temp
    def get_courses_info(self):
        temp = self.data
        del temp[0][0]
        return temp[0]
class Data_Analyzer:
    def __init__(self,obj):
        self.obj = obj
    def get_mean(self,subject):
        temp = self.obj.get_records()
        sum = 0
        exist = False
        if subject == "math":
            for i in range(len(temp)):
                sum += temp[i][1]
            exist = True
            return True, sum / len(temp)
        if subject == "science":
            for i in range(len(temp)):
                sum += temp[i][2]
            exist = True
            return True, sum / len(temp)
        if subject == "programming":
            for i in range(len(temp)):
                sum += temp[i][3]
            exitst = True
            return True, sum / len(temp)
        if exist == False:
            return False, -1
    def get_names(self):
        temp = self.obj.get_records()
        name = []
        for i in range(len(temp)):
            name.append(temp[i][0])
        return name
    def get_name_sorted(self,descending=False):
        temp = self.get_names()
        descending_temp = descending
        if descending_temp == False:
            return sorted(temp,reverse=False)
        if descending_temp == True:
            return sorted(temp,reverse=True)
    def get_best_name_by_score(self):
        sum = []
        temp = self.obj.get_records()
        best_name = 0
        max_score = 0
        for i in range(len(temp)):
            sum.append(temp[i][1] + temp[i][2] + temp[i][3])
        max_score = max(sum)
        for i in range(len(sum)):
            if max_score == sum[i]:
                best_name = temp[i][0]
        return best_name,max_score
    def get_best_name_by_course(self,subject):
        temp = self.obj.get_records()
        record_course = []
        best_name = 0
        best_score = 0
        subject_code = 0
        if subject == "math":
            subject_code = 1
        if subject == "science":
            subject_code = 2
        if subject == "programming":
            subject_code = 3
        if subject_code == 0:
            return -1
        for i in range(len(temp)):
            record_course.append(temp[i][subject_code])
        best_score = max(record_course)
        for i in range(len(temp)):
            if best_score == record_course[i]:
                best_name = temp[i][0]
        return best_name, best_score
    def get_records_sorted_by_name(self,descending=False):
        name_sorted = []
        data_sorted = []
        temp = self.obj.get_records()
        for i in range(len(temp)):
            name_sorted.append(temp[i][0])
        name_sorted.sort(reverse = descending)
        for i in range(len(name_sorted)):
            for j in range(len(name_sorted)):
                if name_sorted[i] == temp[j][0]:
                    data_sorted.append(temp[j])
        return data_sorted

    
    
    
# (A) ANSWER END
############################################################

############################################################
# (B) STANDARD ANSWER START



# (B) STANDARD ANSWER END
############################################################

############################################################
# (C) SCORING START

print('===============================================================================')
print("$$$$ scoring started")
print('===============================================================================')

totalScore = 0

def printAnswers(given_answer, right_answer):
    print("-->> given answer [", given_answer, "] as [", type(given_answer), "]")
    print("     right answer [", right_answer, "] as [", type(right_answer), "]")

####
####

RAW_DATA_STANDARD = [
    'name,math,science,programming', # 항상 첫줄임. 빈칸 없음. 과목은 세과목 한정이며, 과목명 불변
    ['apple',   90, 80, 93], # 학생은 더 추가될 수 있음
    ['orange',  95, 98, 92],
    ['kiwi',    80, 70, 70], 
    ['mango',  100, 97, 90],
    ['banana',  62, 95, 88]
]

RAW_DATA_SCORING = RAW_DATA_STANDARD[:]

####
####

# Scoring 1 : 
#

print("[01] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Data(RAW_DATA_STANDARD)
    d_given = Data(RAW_DATA_SCORING)

    r_standard = d_standard.get()
    r_given = d_given.get()

    if r_standard == r_given:
        print("[01] correct")
        printAnswers(r_given, r_standard)
        totalScore += 5
    else:
        print("[01] fail")
        printAnswers(r_given, r_standard)
except:
    print("[01] exception")

print('===============================================================================')

# Scoring 2 : 
#

print("[02] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    r_standard = d_standard.get()
    r_given = d_given.get()

    if r_standard == r_given and isinstance(d_given, Data):
        print("[02] correct")
        printAnswers(r_given, r_standard)
        totalScore += 5
    else:
        print("[02] fail")
        printAnswers(r_given, r_standard)
except:
    print("[02] exception")

print('===============================================================================')

# Scoring 3 : 
#

print("[03] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    r_standard = d_standard.get_records()
    r_given = d_given.get_records()

    if r_standard == r_given:
        print("[03] correct")
        printAnswers(r_given, r_standard)
        totalScore += 10
    else:
        print("[03] fail")
        printAnswers(r_given, r_standard)
except:
    print("[03] exception")

print('===============================================================================')

# Scoring 4 : 
#

print("[04] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    r_standard = d_standard.get_courses_info()
    r_given = d_given.get_courses_info()

    if r_standard == r_given:
        print("[04] correct")
        printAnswers(r_given, r_standard)
        totalScore += 10
    else:
        print("[04] fail")
        printAnswers(r_given, r_standard)
except:
    print("[04] exception")

print('===============================================================================')

# Scoring 5 : 
#

print("[05] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    da_standard = s.Data_Analyzer(d_standard)
    da_given = Data_Analyzer(d_given)

    f1 = f2 = f3 = f4 = False

    r_standard = da_standard.get_mean('math') 
    r_given = da_given.get_mean('math')

    if r_standard == r_given:
        print("[05] correct 1")
        printAnswers(r_given, r_standard)
        f1 = True
    else:
        print("[05] fail 1")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_mean('science') 
    r_given = da_given.get_mean('science')

    if r_standard == r_given:
        print("[05] correct 2")
        printAnswers(r_given, r_standard)
        f2 = True
    else:
        print("[05] fail 2")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_mean('programming') 
    r_given = da_given.get_mean('programming')

    if r_standard == r_given:
        print("[05] correct 3")
        printAnswers(r_given, r_standard)
        f3 = True
    else:
        print("[05] fail 3")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_mean('english') 
    r_given = da_given.get_mean('english')

    if r_standard == r_given:
        print("[05] correct 4")
        printAnswers(r_given, r_standard)
        f4 = True
    else:
        print("[05] fail 4")
        printAnswers(r_given, r_standard)

    if f1 and f2 and f3 and f4:
        totalScore += 10
except:
    print("[05] exception")

print('===============================================================================')

# Scoring 6 : 
#

print("[06] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    da_standard = s.Data_Analyzer(d_standard)
    da_given = Data_Analyzer(d_given)

    r_standard = da_standard.get_names() 
    r_given = da_given.get_names()

    if r_standard == r_given:
        print("[06] correct")
        printAnswers(r_given, r_standard)
        totalScore += 10
    else:
        print("[06] fail")
        printAnswers(r_given, r_standard)
except:
    print("[06] exception")

print('===============================================================================')

# Scoring 7 : 
#

print("[07] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    da_standard = s.Data_Analyzer(d_standard)
    da_given = Data_Analyzer(d_given)

    f1 = f2 = False

    r_standard = da_standard.get_names_sorted() 
    r_given = da_given.get_names_sorted()

    if r_standard == r_given:
        print("[07] correct 1")
        printAnswers(r_given, r_standard)
        f1 = True
    else:
        print("[07] fail 1")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_names_sorted(descending=True) 
    r_given = da_given.get_names_sorted(descending=True)

    if r_standard == r_given:
        print("[07] correct 2")
        printAnswers(r_given, r_standard)
        f2 = True
    else:
        print("[07] fail 2")
        printAnswers(r_given, r_standard)

    if f1 and f2:
        totalScore += 10
except:
    print("[07] exception")

print('===============================================================================')

# Scoring 8 : 
#

print("[08] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    da_standard = s.Data_Analyzer(d_standard)
    da_given = Data_Analyzer(d_given)

    r_standard = da_standard.get_best_name_by_score() 
    r_given = da_given.get_best_name_by_score()

    if r_standard == r_given:
        print("[08] correct")
        printAnswers(r_given, r_standard)
        totalScore += 10
    else:
        print("[08] fail")
        printAnswers(r_given, r_standard)
except:
    print("[08] exception")

print('===============================================================================')

# Scoring 9 : 
#

print("[09] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    da_standard = s.Data_Analyzer(d_standard)
    da_given = Data_Analyzer(d_given)

    f1 = f2 = f3 = f4 = False

    r_standard = da_standard.get_best_name_by_course('math') 
    r_given = da_given.get_best_name_by_course('math')

    if r_standard == r_given:
        print("[09] correct 1")
        printAnswers(r_given, r_standard)
        f1 = True
    else:
        print("[09] fail 1")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_best_name_by_course('science') 
    r_given = da_given.get_best_name_by_course('science')

    if r_standard == r_given:
        print("[09] correct 2")
        printAnswers(r_given, r_standard)
        f2 = True
    else:
        print("[09] fail 2")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_best_name_by_course('programming') 
    r_given = da_given.get_best_name_by_course('programming')

    if r_standard == r_given:
        print("[09] correct 3")
        printAnswers(r_given, r_standard)
        f3 = True
    else:
        print("[09] fail 3")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_best_name_by_course('english') 
    r_given = da_given.get_best_name_by_course('english')

    if r_standard == r_given:
        print("[09] correct 4")
        printAnswers(r_given, r_standard)
        f4 = True
    else:
        print("[09] fail 4")
        printAnswers(r_given, r_standard)

    if f1 and f2 and f3 and f4:
        totalScore += 10
except:
    print("[09] exception")

print('===============================================================================')

# Scoring 10 : 
#

print("[10] scoring started ...")
print('-------------------------------------------------------------------------------')

try:
    d_standard = s.Filtered_Data(RAW_DATA_STANDARD)
    d_given = Filtered_Data(RAW_DATA_SCORING)

    da_standard = s.Data_Analyzer(d_standard)
    da_given = Data_Analyzer(d_given)

    f1 = f2 = False

    r_standard = da_standard.get_records_sorted_by_name() 
    r_given = da_given.get_records_sorted_by_name()

    if r_standard == r_given:
        print("[10] correct 1")
        printAnswers(r_given, r_standard)
        f1 = True
    else:
        print("[10] fail 1")
        printAnswers(r_given, r_standard)

    r_standard = da_standard.get_records_sorted_by_name(descending=True) 
    r_given = da_given.get_records_sorted_by_name(descending=True)

    if r_standard == r_given:
        print("[10] correct 2")
        printAnswers(r_given, r_standard)
        f2 = True
    else:
        print("[10] fail 2")
        printAnswers(r_given, r_standard)

    if f1 and f2:
        totalScore += 10
except:
    print("[10] exception")

print('===============================================================================')

# FINAL SCORE
print("$$$$ 채점 점수 (90점 만점 기준) :", totalScore, "점")
print('===============================================================================')
print("$$$$ 최종 성적 반영 점수 (70점 기준 - 강의계획서 참조) :", int(totalScore / 9.0 * 7.0), '점')
print('===============================================================================')

# (C) SCORING END
############################################################
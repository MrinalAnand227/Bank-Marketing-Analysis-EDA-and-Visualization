#!/usr/bin/env python
# coding: utf-8

# ## PERFORMING EXPLORATORY DATA ANALYSIS ON BANK MARKETING ANALYTICS

# **STEP.01= IMPORTING LIBRARY(PANDAS)**

# In[4]:


# Importing Library

import pandas as pd,os


# **STEP.02 = LOADING DATASET INTO NOTEBOOK**

# In[5]:


#HERE df is dataframe in PANDAS

bank_df = pd.read_excel('C:\\Users\\abc\\Documents\\MARCH 2022 - NEW\\INTERNSHIP @ INEURON\\BANKING PROJECT\\bankfull1.xlsx')


# **STEP.03= CHECKING THE FIRST 5 AND LAST 5 ROWS OF THE DATASET, using head() & tail()**
# 

# In[6]:


#head
bank_df.head()


# In[17]:


#tail
bank_df.tail()


# **STEP.04= CHECKING THE DATAYPE & OTHER INFO OF THE DATASET**
# 
# 

# In[7]:


bank_df.info()


# **STEP.05= CHECKING THE NULL VALUES OF THE DATASET**

# In[8]:


bank_df.isnull().sum() #this will return the count of null from each columns.

Since in the given dataset it is mentioned that the null values are present as 'unknown' instead of 'nan/NaN/NuLL', 
thus it is not showing the result.
# **STEP.06= LET'S RENAME THE VARIOUS COLUMNS FOR BETTER UNDERSTANDING**

# In[9]:


#using .rename(columns = {'col1':'new_name'},inplace = true)

bank_df.rename(columns ={'age':'Age_Group','job':'Job_Types','housing':'Housing_Loan','loan':'Personal_Loan'}, inplace = True)
bank_df.rename(columns = {'duration':'Last_Call_Dur','campaign':'Current_FollowUps','pdays':'Contact_Day_Diff'}, inplace = True)
bank_df.rename(columns = {'previous':'Previous_FollowUps', 'poutcome':'Previous_Camp_Status', 'y':'Current_Camp_Status'}, 
                           inplace =True)


# In[10]:


bank_df.head()


# **STEP.07= CATERGORIZING THE NUMERIC COLUMNS IN ORDER TO FIND KEY RELATIONSHIPS GOING AHEAD**
Now this is a very lengthy step, since it requires all the operations to be performed column by columns.
# **STEP.07.1= CREATING FUNCTION FOR (AGE GROUP)**
# 
# **x(18-30):Young Adults, x(31-45):Min Age Adults, x(46-60): Veterans, x(>60): Senior Citizen**
# 

# In[11]:


#creating a function.

def age_group(x):
    if x >=18 and x<=30:
        return 'Young Adults'
    elif x>30 and x<=45:
        return 'Mid Age Adults'
    elif x>45 and x<=60:
        return 'Veterans'
    else:
        return 'Senior Citizen'


# In[12]:


#applying function to the column

bank_df['Age_Group'] = bank_df['Age_Group'].apply(age_group)


# In[13]:


#checking value counts after categorizing

bank_df['Age_Group'].value_counts()


# **STEP.07.2= CHECKING THE VALUE COUNTS IN (JOB TYPES) & TREATING THE MISSING VALUES WITH MODE**

# In[14]:


bank_df.Job_Types.value_counts() #Or use { bank_df['Job_Types'].value_counts() }

Above we can see there are 288 unknown null values available in the Job category and it may affect the outcome, so we need to treat them with Mode of the column, since the records are categorical in nature.
# In[15]:


#Finding the mode, so that we can replace it with unknown entires.

bank_df.Job_Types.mode() #or write bank_df['Job_Types'].mode()


# In[16]:


#Replacing null value with mode column by creating the function

def unknown2bluecollar(x):
    if x == 'unknown':
        return 'blue-collar'
    else:
        return x


# In[17]:


#Applying function on Job_Type

bank_df['Job_Types'] = bank_df['Job_Types'].apply(unknown2bluecollar)


# In[18]:


#Checking after replacing the unknowns with mode

bank_df['Job_Types'].value_counts()


# In[19]:


bank_df['Job_Types'].unique()


# **STEP.07.2.1= Grouping the Job_Types into White Collar Job/ Blue Collar Job/ Entrepreneur**
•Creating function for job group
                    •considered desk job as white collar job
                    •considerd field job as blue collar job
                    •considerd self-employed as Entrepreneur  
# In[20]:


def job_group(x):
    if x == 'admin.' or x == 'management' or x == 'services':
        return 'White Collar'
    elif x == 'blue-collar' or x  == 'housemaid' or x == 'technician':
        return 'Blue Collar'
    elif x == 'entrepreneur' or x == 'self-employed':
        return 'Entrepreneur'
    else:
        return x


# In[21]:


#Applying the grouping function

bank_df['Job_Types'] = bank_df['Job_Types'].apply(job_group)


# In[22]:


#checking the result after applying the function.

bank_df.Job_Types.value_counts()


# **STEP.07.3= CHECKING AND TREATING THE MISSING VALUES FROM EDUCATION COLUMN**

# In[23]:


#checking  null values from column

bank_df['education'].value_counts()


# **The above result shows there are 928 unknown entries, to treat them we need to replace them with MODE of the column**

# In[24]:


#finding the mode of education

bank_df.education.mode()


# In[25]:


#Replacing null value with mode column by creating the function

def replace_edu(x):
    if x == 'unknown':
        return 'secondary'
    else:
        return x


# In[26]:


#Applying the function to replace the unknown.

bank_df.education = bank_df.education.apply(replace_edu)


# In[27]:


#checking the result after removing the null values.

bank_df['education'].value_counts()


# **STEP.07.4= CHECKING, GROUPING & TREATING THE MISSING VALUES FROM THE BALANCE COLUMN**
Since all the entries in the Balance are nurmeric thus we will first define a function for the grouping and then apply the grouping to the balance column
# •considered value **< 0** as **negative balance**
# 
# •considerd value **> 0** and **<= 500** as **low balance**
# 
# •considerd value **> 500** and **<= 4000** as **average balance**
# 
# •considerd value **> 4000**  as **high  balance**

# In[28]:


#Creating grouping function for balance

def group_bal(y):
    if y <= 0:
        return 'Negative balance'
    elif (y > 0 and y <= 500):
        return 'Low Balance'
    elif (y > 500 and y <= 4000):
        return 'Average Balance'
    else:
        return 'High Balance'


# In[29]:


#Applying the grouping function to the education column.

bank_df.balance=bank_df.balance.apply(group_bal)


# In[30]:


bank_df.balance.value_counts()


# **STEP.07.5= CONVERTING THE VALUES IN THE Last_Call_Duration COLUMN FROM SECONDS TO MINTUES & ROUNDING TO 0.**

# In[31]:


#dividing the column with 60 to get values in minutes and using .round(0) function.

bank_df.Last_Call_Dur = (bank_df.Last_Call_Dur / 60).round(0)


# In[32]:


#checking the changes in Last_Call_Dur column

bank_df


# **STEP.07.5.1= GROUPING THE VALUES IN THE Last_Call_Duration COLUMN**
# 
# •considerd duration **>= 0** and **<= 2** as **short call time**
# 
# •considerd duration **> 2** and **<= 5** as **medium call time**
# 
# •considerd duration  **> 5** as **high call time**

# In[33]:


#Function for grouping the Last_Call_Dur

def group_LCD(z):
    if (z>=0 and z<=2):
        return 'short call time'
    elif (z>2 and z<=5):
        return 'medium call time'
    else:
        return 'high call time'


# In[34]:


#applying the grouping to the column

bank_df.Last_Call_Dur = bank_df.Last_Call_Dur.apply(group_LCD)


# In[81]:


#Checking the update on the column

bank_df


# In[35]:


bank_df.Last_Call_Dur.value_counts()


# **STEP.07.6= DROPPING THE CONTACT COLUMN, SINCE IT IS NOT HELPING TO ANALYSE ANYTHING.**

# In[36]:


#use .drop(['col_name'], axis=1, inplace =true)

bank_df.drop(['contact'],axis=1 ,inplace = True)


# In[37]:


bank_df


# **STEP.07.7= GROUPING THE Current_FollowUps Column**
# 
# •cosidered value **>0** and **<=5** as **upto 5 followups**
# 
# •considered value **>5** as **more than 5 followups**

# In[38]:


#Fuction for grouping the Current_FollowUps

def group_followup(x):
    if (x>0 and x<=5):
        return 'Upto 5 followups'
    else:
        return 'More than 5 followups'


# In[39]:


#Applying the function to the respective column

bank_df.Current_FollowUps = bank_df.Current_FollowUps.apply(group_followup)


# In[40]:


bank_df.Current_FollowUps.value_counts()


# In[41]:


bank_df


# **STEP.07.8= GROUPING THE Contact_Day_Diff Column**
# 
# •consider values **=-1** as **Not Contacted**
# 
# •consider values **>=0** and **<=90** as **0-3 Months Back**
# 
# •consider values **>90** and **<=180** as **3-6 Months Back**
# 
# •consider values **>180** as **More Than 6 Months**

# In[42]:


# creating function for Contact_Day_Diff column group

def group_CDF(x):
    if x == -1:
        return 'Not Contacted'
    elif x >= 0 and x <= 90:
        return '0-3 Months Back'
    elif x > 90 and x <= 180:
        return '3-6 Months Back'
    else:
        return 'More Than 6 Months'


# In[43]:


#Applying the function to the column

bank_df.Contact_Day_Diff = bank_df.Contact_Day_Diff.apply(group_CDF)


# In[44]:


bank_df.Contact_Day_Diff.value_counts()


# In[91]:


bank_df


# **STEP.07.9= GROUPING THE Previous_FollowUps Column**
# 
# •cosidered value **>=0** and **<=5** as **upto 5 followups**
# 
# •considered value **>5** as **more than 5 followups**
# 
# 

# In[48]:


#Function for grouping the previous followups column

def previous_followup(x):
    if x >= 0 and x <=5:
        return 'Upto 5 followups'
    else:
        return 'More Than 5 followups'


# In[49]:


bank_df.Previous_FollowUps = bank_df.Previous_FollowUps.apply(previous_followup)


# In[50]:


bank_df.Previous_FollowUps.value_counts() 


# In[51]:


bank_df.Previous_FollowUps.unique()


# In[52]:


bank_df


# **STEP.07.10= OPERATING THE Previous_camp_Status COLUMN**
# 
# •**We need to the check the view counts and uniqueness of the entries**
# 
# •**Replacing null values (i.e 'unknown') with not contacted and (others) with failure**

# In[55]:


bank_df.Previous_Camp_Status.unique()


# In[56]:


bank_df.Previous_Camp_Status.value_counts()

The above result shows we have 36k 'unknown' records, we will consider them as Not Contacted

& 1.8k 'other' does not defines anything, thus we will consider it as a failure. 
# In[57]:


#replacing the unwanted records: unknown=Not Contacted, other=failure

bank_df.Previous_Camp_Status = bank_df.Previous_Camp_Status.replace('unknown','not contacted').replace('other','failure')


# In[59]:


#Checking the changes after replacement

bank_df.Previous_Camp_Status.value_counts()


# In[60]:


#Suppose replacing the categories once again to assign meaningfull name

bank_df.Previous_Camp_Status=bank_df.Previous_Camp_Status.replace('success','P Subscribed').replace('failure','P N Subscribed')


# In[61]:


#Checking the changes after replacement 2.o


bank_df.Previous_Camp_Status.value_counts()


# In[62]:


bank_df


# **STEP.07.11= OPERATING THE Current_Camp_Status COLUMN**
# 
# •**Replacing yes** = **Subscribed** & **no** = **Not Subscribed**
# 
# 

# In[63]:


bank_df.Current_Camp_Status = bank_df.Current_Camp_Status.replace('yes','Subscribed').replace('no','Not Subscribed ')


# In[64]:


bank_df.Current_Camp_Status.value_counts()


# In[65]:


bank_df

TILL HERE, WE HAVE PERFORMED THE EXPLORATORY DATA ANALYSIS AND WE HAVE GOT THE FINAL CLEANED TABLE WHICH HAS BEEN CATEGORIZED.
# **STEP.08 = SAVE THE FILE**
# 
# **Now it's time to save the file, so that we can perform data visualization after hooking up to POWER BI**

# In[69]:


bank_df.to_csv('Final_Banking_file.csv')


# In[ ]:





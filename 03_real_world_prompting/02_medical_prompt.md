# 第 2 課：真實世界的提示詞

在上一課中，我們討論了幾個關鍵的提示技巧，並分別示範了各自的使用方法。現在讓我們嘗試撰寫一個更大型的提示詞，融合我們剛才學到的多種技巧。

---

## 我們的提示目標
本課將專注於撰寫一個醫療病歷摘要提示詞，能夠接收冗長的病歷資料，並生成包含重要資訊的摘要，協助醫師準備即將到來的門診預約。

每份病人病歷的內容大致如下：

```
Patient Name: Evelyn Thompson
Age: 78
Medical Record:

1985: Diagnosed with type 2 diabetes, started on metformin
1992: Developed hypertension, prescribed lisinopril
1998: Total hip replacement (right) due to osteoarthritis
2000: Diagnosed with hypothyroidism, started on levothyroxine
2003: Cataract surgery (both eyes)
2005: Admitted for atrial fibrillation, started on warfarin
2008: Vitamin B12 deficiency diagnosed, monthly injections started
2010: Increased metformin dose due to rising A1C levels
2011: Admitted for transient ischemic attack (TIA), added aspirin to regimen
2013: Diagnosed with stage 2 breast cancer, underwent lumpectomy and radiation
2014: Started on anastrozole for breast cancer recurrence prevention
2015: Developed chronic kidney disease (CKD) stage 3, metformin adjusted
2017: Total knee replacement (left) due to osteoarthritis
2018: Hospitalized for pneumonia, treated with IV antibiotics
2019: Mild cognitive impairment noted, started on donepezil
2020: Lisinopril dosage increased due to refractory hypertension
2021: Recurrent UTIs, prescribed low-dose prophylactic antibiotics
2022: Annual mammogram clear, but eGFR shows worsening kidney function
2023: Mobility declining, started physical therapy and home health aide visits
```

我們的最終目標是生成格式一致的病歷摘要，協助醫療人員準備即將到來的門診預約。每份摘要應包含以下關鍵資訊：

* 病人姓名
* 病人年齡
* 主要診斷
* 病人目前用藥清單
* 近期關注事項
* 醫療人員的待辦事項

以上述病歷為例，輸出結果可能如下所示：

```
Name: Evelyn Thompson
Age: 78

Key Diagnoses:
- Type 2 Diabetes (1985)
- Hypertension (1992)
- Osteoarthritis (Hip and Knee Replacements in 1998 and 2017)
- Hypothyroidism (2000)
- Atrial Fibrillation (2005)
- Vitamin B12 Deficiency (2008)
- Transient Ischemic Attack (TIA) (2011)
- Breast Cancer (2013)
- Chronic Kidney Disease (CKD) Stage 3 (2015)
- Pneumonia (2018)
- Mild Cognitive Impairment (2019)
- Recurrent Urinary Tract Infections (UTIs) (2021)

Medications:
- Metformin (Diabetes)
- Lisinopril (Hypertension)
- Levothyroxine (Hypothyroidism)
- Warfarin (Atrial Fibrillation)
- Aspirin (Antiplatelet)
- Anastrozole (Breast Cancer Recurrence Prevention)
- Donepezil (Cognitive Impairment)
- Low-dose Prophylactic Antibiotics (Recurrent UTIs)

Other Treatments:
- Total Hip Replacement (1998)
- Cataract Surgery (2003)
- Vitamin B12 Injections (2008)
- Lumpectomy and Radiation (Breast Cancer, 2013)
- Total Knee Replacement (2017)
- Physical Therapy and Home Health Aide (2023)

Recent Concerns:
- Worsening Kidney Function (eGFR Decline in 2022)
- Declining Mobility (2023)

Action Items:
- Monitor Kidney Function and Adjust Medications as Needed
- Continue Physical Therapy and Home Health Support
- Evaluate for Cognitive Decline and Adjust Treatment Plan
- Address Mobility Issues and Fall Risk
- Ensure Adherence to Recommended Cancer Screening
```

以下是一個包含 5 份病歷的 Python 清單，我們將用它來測試提示詞：

```python
patient_records = [
    """
Patient Name: Evelyn Thompson
Age: 78
Medical Record:

1985: Diagnosed with type 2 diabetes, started on metformin
1992: Developed hypertension, prescribed lisinopril
1998: Total hip replacement (right) due to osteoarthritis
2000: Diagnosed with hypothyroidism, started on levothyroxine
2003: Cataract surgery (both eyes)
2005: Admitted for atrial fibrillation, started on warfarin
2008: Vitamin B12 deficiency diagnosed, monthly injections started
2010: Increased metformin dose due to rising A1C levels
2011: Admitted for transient ischemic attack (TIA), added aspirin to regimen
2013: Diagnosed with stage 2 breast cancer, underwent lumpectomy and radiation
2014: Started on anastrozole for breast cancer recurrence prevention
2015: Developed chronic kidney disease (CKD) stage 3, metformin adjusted
2017: Total knee replacement (left) due to osteoarthritis
2018: Hospitalized for pneumonia, treated with IV antibiotics
2019: Mild cognitive impairment noted, started on donepezil
2020: Lisinopril dosage increased due to refractory hypertension
2021: Recurrent UTIs, prescribed low-dose prophylactic antibiotics
2022: Annual mammogram clear, but eGFR shows worsening kidney function
2023: Mobility declining, started physical therapy and home health aide visits
    """,
    """
Patient Name: Marcus Reyes
Age: 42
Medical Record:

2001: Diagnosed with generalized anxiety disorder (GAD), started on paroxetine
2003: Diagnosed with major depressive disorder (MDD), added bupropion
2005: Hospitalized for suicidal ideation, added cognitive behavioral therapy (CBT)
2007: Diagnosed with attention-deficit/hyperactivity disorder (ADHD), started on methylphenidate
2009: Reported side effects from paroxetine, switched to escitalopram
2012: Diagnosed with obstructive sleep apnea (OSA), started CPAP therapy
2014: Diagnosed with hypertension, started on losartan
2015: Weight gain noted, referred to nutritionist
2016: Diagnosed with type 2 diabetes, started on metformin
2017: Hospitalized for diabetic ketoacidosis (DKA), insulin therapy initiated
2018: Reported nightmares, switched from bupropion to venlafaxine
2019: Gastroesophageal reflux disease (GERD) diagnosis, started on omeprazole
2020: Divorce, increased therapy sessions, added dialectical behavior therapy (DBT)
2021: Developed plantar fasciitis, prescribed orthotics and physical therapy
2022: Admitted for panic attack, mistaken for myocardial infarction, cardiac workup negative
2023: Attempted suicide, inpatient psychiatric treatment for 30 days
2023: Post-discharge, started on new antipsychotic (quetiapine) and mood stabilizer (lamotrigine)
2024: Reports improvement in mood and sleep, weight loss noted
2024: A1C levels improved, insulin dose decreased
    """,
    """
Patient Name: Lily Chen
Age: 8
Medical Record:

2016 (Birth): Born at 34 weeks, diagnosed with Tetralogy of Fallot (TOF)
  - Immediate surgery to place a shunt for increased pulmonary blood flow
2016 (3 months): Echocardiogram showed worsening right ventricular hypertrophy
2017 (8 months): Complete repair of TOF (VSD closure, pulmonary valve replacement, RV outflow tract repair)
2017 (10 months): Developed post-operative arrhythmias, started on amiodarone
2018 (14 months): Developmental delay noted, referred to early intervention services
2018 (18 months): Speech therapy initiated for delayed language development
2019 (2 years): Diagnosed with failure to thrive, started on high-calorie diet
2019 (2.5 years): Occupational therapy started for fine motor skill delays
2020 (3 years): Cardiac catheterization showed mild pulmonary stenosis
2020 (3.5 years): Diagnosed with sensory processing disorder (SPD)
2021 (4 years): Started integrated preschool program with IEP (Individualized Education Plan)
2021 (4.5 years): Hospitalized for RSV bronchiolitis, required brief oxygen support
2022 (5 years): Echocardiogram showed progression of pulmonary stenosis, balloon valvuloplasty performed
2022 (5.5 years): Diagnosed with attention-deficit/hyperactivity disorder (ADHD), started behavioral therapy
2023 (6 years): Cochlear implant surgery for sensorineural hearing loss
2023 (7 years): Started mainstream school with continued IEP support
2024 (7.5 years): Occupational therapy discontinued, met fine motor skill goals
2024 (8 years): Periodic cardiac follow-up shows stable pulmonary valve function
2024 (8 years): Speech development progressing well, ongoing therapy
    """,
    """
Patient Name: Jason Tran
Age: 25
Medical Record:

2010 (11 yrs): Diagnosed with asthma, started on albuterol inhaler
2012 (13 yrs): First football concussion, brief loss of consciousness
2013 (14 yrs): Fractured right tibia during soccer, surgical fixation
2014 (15 yrs): Second concussion, resulting in post-concussion syndrome
  - Symptoms: headaches, dizziness, memory problems
  - Referred to pediatric neurologist, cognitive rehabilitation therapy
2015 (16 yrs): Developed anxiety and depression, started on fluoxetine
2016 (17 yrs): ACL tear (left knee) during basketball, reconstructive surgery
  - 6-month rehabilitation, switched to non-contact sports
2017 (18 yrs): Graduated high school, started college on academic scholarship
2018 (19 yrs): Diagnosed with PTSD related to sports injuries
  - Started cognitive-behavioral therapy (CBT)
2019 (20 yrs): Tried to return to basketball, experienced panic attack
  - Increased therapy sessions, added exposure therapy
2020 (21 yrs): COVID-19 pandemic, remote learning, reported increased anxiety
  - Started mindfulness meditation and yoga
2021 (22 yrs): Diagnosed with sleep apnea, started CPAP therapy
  - Sleep study suggested link between concussions and sleep disorder
2022 (23 yrs): Gradual return to low-impact sports (swimming, cycling)
  - Reported improved mood and sleep quality
2023 (24 yrs): Graduated college, started job in sports analytics
  - Continuing therapy, now biweekly
  - Volunteering with youth concussion awareness program
2024 (25 yrs): Annual check-up - asthma well-controlled, mental health stable
  - No sports-related injuries in past 2 years
  - Training for first half-marathon
    """,
    """
Patient Name: Amira Khan
Age: 36
Medical Record:

2011: Recurrent joint pain and fatigue, initial diagnosis of fibromyalgia
  - Started on pregabalin and physical therapy
2012: Developed persistent rash and photosensitivity
  - Dermatologist diagnosed cutaneous lupus (CLE)
  - Started on topical corticosteroids and sunscreen
2013: Complained of severe fatigue, hair loss, and cognitive issues ("brain fog")
  - Blood tests showed positive ANA and anti-dsDNA antibodies
  - Diagnosed with Systemic Lupus Erythematosus (SLE)
  - Started on hydroxychloroquine and low-dose prednisone
2014: Hospitalized for lupus nephritis (class III)
  - Renal biopsy confirmed diagnosis
  - Started on mycophenolate mofetil and increased prednisone
2015: Developed interstitial lung disease (ILD) secondary to SLE
  - Started on cyclophosphamide pulse therapy
  - Required home oxygen therapy
2016: Diagnosed with secondary Sjögren's syndrome
  - Symptoms: dry eyes, dry mouth
  - Started on pilocarpine and artificial tears
2017: Hospitalized for lupus cerebritis
  - Symptoms: seizures, confusion, memory loss
  - MRI showed brain inflammation
  - Treated with high-dose steroids and rituximab
2018: Developed avascular necrosis (AVN) of hip, steroid-induced
  - Underwent total hip replacement surgery
2019: Started on belimumab to reduce flare frequency
  - Gradual reduction in prednisone dosage
2020: COVID-19 pandemic, self-isolated due to immunosuppression
  - Telemedicine follow-ups, home infusions
2021: Diagnosed with steroid-induced diabetes
  - Started on metformin and insulin
  - Referred to endocrinologist and nutritionist
2022: Flare-up of lupus, increased joint pain and fatigue
  - Adjusted medications: increased mycophenolate, added abatacept
2023: Cardiovascular screening due to long-term steroid use
  - Echo showed early signs of diastolic dysfunction
  - Started on ACE inhibitors, referred to cardio-rehab
2024: Improvement noted in all organ systems
  - Tapering immunosuppressants, monitoring closely
  - Continues physical therapy, yoga for joint health
  - Planning pregnancy, consulted with high-risk OB
    """
]
```

讓我們先看一份，確認清單運作正常：

```python
patient_records[2]
```

```
'\nPatient Name: Lily Chen\nAge: 8\nMedical Record:\n\n2016 (Birth): Born at 34 weeks, diagnosed with Tetralogy of Fallot (TOF)\n  - Immediate surgery to place a shunt for increased pulmonary blood flow\n2016 (3 months): Echocardiogram showed worsening right ventricular hypertrophy\n2017 (8 months): Complete repair of TOF (VSD closure, pulmonary valve replacement, RV outflow tract repair)\n2017 (10 months): Developed post-operative arrhythmias, started on amiodarone\n2018 (14 months): Developmental delay noted, referred to early intervention services\n2018 (18 months): Speech therapy initiated for delayed language development\n2019 (2 years): Diagnosed with failure to thrive, started on high-calorie diet\n2019 (2.5 years): Occupational therapy started for fine motor skill delays\n2020 (3 years): Cardiac catheterization showed mild pulmonary stenosis\n2020 (3.5 years): Diagnosed with sensory processing disorder (SPD)\n2021 (4 years): Started integrated preschool program with IEP (Individualized Education Plan)\n2021 (4.5 years): Hospitalized for RSV bronchiolitis, required brief oxygen support\n2022 (5 years): Echocardiogram showed progression of pulmonary stenosis, balloon valvuloplasty performed\n2022 (5.5 years): Diagnosed with attention-deficit/hyperactivity disorder (ADHD), started behavioral therapy\n2023 (6 years): Cochlear implant surgery for sensorineural hearing loss\n2023 (7 years): Started mainstream school with continued IEP support\n2024 (7.5 years): Occupational therapy discontinued, met fine motor skill goals\n2024 (8 years): Periodic cardiac follow-up shows stable pulmonary valve function\n2024 (8 years): Speech development progressing well, ongoing therapy\n    '
```

---

## 我們最初的「糟糕」提示詞

讓我們先從一個非常簡單的提示詞開始，請 Claude 生成摘要。最初的嘗試可能如下所示：

> I have this patient medical record. Can you summarize it for me?
> 
> {medical record goes here}
> 
> I need this for a quick review before the patient's appointment tomorrow.

讓我們將這個想法正式化，寫成一個可以動態插入病歷的提示詞：

```python
initial_prompt = """
I have this patient medical record. Can you summarize it for me?

{record}

I need this for a quick review before the patient's appointment tomorrow.
"""
```

接下來，我們撰寫一個簡單的函式，接收單份病歷，將其插入提示詞，並請 Claude 生成摘要：

```python
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def generate_summary_with_bad_prompt(patient_record):
    prompt_with_record = initial_prompt.format(record=patient_record)
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt_with_record}]
    )
    print("===============================")
    print(response.content[0].text)
```

讓我們用 `patient_records` 清單中的 5 份病歷全部測試看看：

```python
generate_summary_with_bad_prompt(patient_records[0])
```

```
===============================
Here is a summary of Evelyn Thompson's 78-year-old medical record:

Chronic Conditions:
- Type 2 diabetes (since 1985) - on metformin, dose increased in 2010
- Hypertension (since 1992) - on lisinopril, dose increased in 2020
- Hypothyroidism (since 2000) - on levothyroxine  
- Atrial fibrillation (since 2005) - on warfarin
- Vitamin B12 deficiency (since 2008) - receiving monthly injections
- Chronic kidney disease stage 3 (since 2015) - metformin adjusted
- Mild cognitive impairment (since 2019) - on donepezil

Surgical History:
- Total hip replacement (1998) - right side, due to osteoarthritis
- Cataract surgery (2003) - both eyes
- Lumpectomy and radiation (2013) - for stage 2 breast cancer  
- Total knee replacement (2017) - left side, due to osteoarthritis

Cancer History: 
- Breast cancer (2013) - currently on anastrozole for recurrence prevention

Recent Issues:
- Recurrent UTIs (2021) - on prophylactic antibiotics
- Worsening kidney function per eGFR (2022)
- Declining mobility (2023) - started physical therapy and home health aide

Overall, an elderly patient with multiple chronic conditions requiring polypharmacy and close monitoring, especially for diabetes, hypertension, kidney disease, and cancer recurrence.
```

```python
generate_summary_with_bad_prompt(patient_records[1])
```

```
===============================
Here's a summary of Marcus Reyes' (age 42) medical record:

Mental Health:
- Diagnosed with generalized anxiety disorder in 2001, treated with paroxetine
- Major depressive disorder diagnosed in 2003, bupropion added
- Hospitalized for suicidal ideation in 2005, started cognitive behavioral therapy (CBT)  
- ADHD diagnosis in 2007, started methylphenidate
- Medications changed over time due to side effects/inefficacy (escitalopram, venlafaxine, quetiapine, lamotrigine)
- Attempted suicide in 2023, required 30-day inpatient psychiatric treatment
- Divorce in 2020 led to increased therapy (added dialectical behavior therapy)

Other Conditions:
- Obstructive sleep apnea in 2012, started CPAP therapy
- Hypertension in 2014, started losartan  
- Weight gain, referred to nutritionist in 2015
- Type 2 diabetes diagnosed in 2016, metformin started
- Hospitalized for diabetic ketoacidosis in 2017, insulin initiated
- GERD diagnosed in 2019, started omeprazole
- Plantar fasciitis in 2021, prescribed orthotics and physical therapy
- Panic attack in 2022, mistaken for heart attack

Recent Updates:  
- 2024: Mood and sleep improved, weight loss noted
- 2024: A1C levels improved, insulin dose decreased

The patient has a complex medical history involving multiple psychiatric conditions managed with medications and therapy. He also has several chronic conditions like diabetes, hypertension, and sleep apnea that require management.
```

```python
generate_summary_with_bad_prompt(patient_records[2])
```

```
===============================
Here is a summary of Lily Chen's 8-year medical record:

Lily was born prematurely at 34 weeks in 2016 with Tetralogy of Fallot (TOF), a congenital heart defect. She underwent immediate surgery for a shunt and then complete TOF repair at 8 months old in 2017. Post-operatively, she developed arrhythmias requiring medication.

Starting around 1 year old, Lily experienced developmental delays - failure to thrive, speech/language delays requiring therapy, fine motor skill delays requiring occupational therapy, and a sensory processing disorder diagnosis. An IEP was started in preschool for extra support.

Cardiac issues continued with mild pulmonary stenosis at 3 years old, requiring a balloon valvuloplasty at 5 years. She was also diagnosed with ADHD at 5.5 years and started behavioral therapy.

Other medical events included an RSV bronchiolitis hospitalization at 4.5 years requiring oxygen, and cochlear implant surgery at 6 years for sensorineural hearing loss.

Now at 8 years old, Lily has stable cardiac function but continues speech therapy. She has met fine motor goals and receives mainstream schooling with an IEP.
```

```python
generate_summary_with_bad_prompt(patient_records[3])
```

```
===============================
Here is a summary of Jason Tran's 25-year-old medical record:

Asthma & Sports Injuries
- Diagnosed with asthma at age 11, prescribed albuterol inhaler
- Multiple sports concussions starting at age 13, with post-concussion syndrome 
- Fracture and knee injuries requiring surgery in teens

Mental Health
- Developed anxiety and depression at 16, started fluoxetine
- Diagnosed with PTSD at 19 related to sports injuries, started CBT and exposure therapy
- Experienced panic attack at 20 trying to return to basketball
- Increased anxiety during COVID-19 pandemic at 21, started mindfulness practices

Sleep Issues
- Diagnosed with sleep apnea at 22 potentially linked to concussions, started CPAP

Recent Updates
- Gradual return to low-impact sports at 23 with improved mood/sleep
- Graduated college at 24, working in sports analytics 
- Continuing biweekly therapy and youth concussion awareness program
- Training for first half-marathon at 25, asthma and mental health stable

Key Issues
- History of asthma
- Multiple concussions and sports injuries 
- Anxiety, depression, PTSD 
- Sleep apnea

I've highlighted the key medical issues, mental health conditions, and recent progress to prepare for tomorrow's appointment. Let me know if you need any clarification or have additional details to add.
```

```python
generate_summary_with_bad_prompt(patient_records[4])
```

```
===============================
Here is a summary of Amira Khan's lengthy and complex medical history:

Amira Khan is a 36-year-old woman with a long-standing diagnosis of Systemic Lupus Erythematosus (SLE). Her initial symptoms in 2011 were joint pain and fatigue. After developing rashes and photosensitivity in 2012, she was diagnosed with cutaneous lupus and started on topical steroids. In 2013, positive autoantibodies and multi-system involvement led to the SLE diagnosis.

Over the years, Amira has experienced numerous lupus complications affecting multiple organs:
- Lupus nephritis requiring immunosuppressants (2014)
- Interstitial lung disease requiring cyclophosphamide and oxygen (2015)  
- Secondary Sjogren's syndrome (2016)
- Lupus cerebritis with brain inflammation (2017)
- Avascular necrosis of hip requiring joint replacement (2018)

She has required intensive treatment with hydroxychloroquine, mycophenolate, cyclophosphamide, rituximab, belimumab, and long-term corticosteroids leading to side effects like diabetes and diastolic dysfunction. Despite treatment challenges, her condition has gradually improved with multi-disciplinary care.

Currently, she is on abatacept, mycophenolate, ACE inhibitors, and trying to taper corticosteroids. She continues physical therapy and is interested in a future pregnancy consultation. Close monitoring is needed for her complex multi-system disease and medication side effects.
```

仔細查看 Claude 生成的摘要，會發現格式參差不齊！有些摘要是長篇段落，有些則是條列式清單。每份摘要的實際內容也差異極大。摘要內容本身還算不錯，但格式、長度以及摘要資料的類型都不一致，很難以程式化方式使用。讓我們來改進它！

---

## 改進提示詞

如我們在上一課所學，有一套清晰的提示技巧可以幫助我們獲得更好、更一致的結果，包括：

* 加入清楚的系統提示詞，為助理設定情境和角色，例如醫療專業人員或醫療資料分析師
* 使用 XML 標籤（例如 `<patient_record>`）結構化輸入資料，讓提示詞中哪部分是輸入資料一目瞭然
* 提供清楚、具體的指示，說明摘要應涵蓋哪些重點，例如診斷、用藥和近期健康問題
* 指定摘要的期望格式，例如條列式或有特定分區的結構化格式
* 提供格式良好的摘要範例，引導助理的回應
* 使用某種輸出 XML 標籤來結構化輸出內容，讓使用者能快速找到相關資訊

**在後續課程中，我們將討論一種針對提示工程和選擇提示技巧的具體、細緻的方法。本課中，我們將採用「廣撒網」的方式，一次使用所有技巧。**

### 加入系統提示詞
讓我們逐一處理這些建議。首先定義系統提示詞，為助理設定情境和角色。根據我們的經驗，系統提示詞只應放入這些資訊。

對於我們的使用情境，系統提示詞應告訴 Claude，其角色是扮演一位擅長將冗長病史轉化為簡潔摘要的醫療專業人員。

以下是一種做法：

```python
system = """
You are a highly experienced medical professional with a specialty in translating complex patient histories into concise, actionable summaries. 
Your role is to analyze patient records, identify critical information, and present it in a clear, structured format that aids in diagnosis and treatment planning. 
Your summaries are invaluable for busy healthcare providers who need quick insights into a patient's medical history before appointments.
"""
```

### 結構化輸入資料
使用 Claude 時，最重要的提示技巧之一就是用 XML 標籤清楚標記輸入資料。在我們目前的提示詞中，主要輸入資料是這樣提供的：

> I have this patient medical record. Can you summarize it for me?
> 
> {medical record goes here}
> 
> I need this for a quick review before the patient's appointment tomorrow.

一個能帶來顯著改善的簡單做法，是用 XML 標籤包裹輸入資料。讓我們使用 `<patient_record>` 標籤來更新提示詞：

```python
#System Prompt
system = """
You are a highly experienced medical professional with a specialty in translating complex patient histories into concise, actionable summaries. 
Your role is to analyze patient records, identify critical information, and present it in a clear, structured format that aids in diagnosis and treatment planning. 
Your summaries are invaluable for busy healthcare providers who need quick insights into a patient's medical history before appointments.
"""

#Improved Prompt (still a work in progress!)
updated_prompt = """
<patient_record>
{record}
</patient_record>
"""
```

### 提供清楚的指示
使用 Claude 時，提供清楚直接的指示對於獲得最佳結果至關重要。就像第一次指導一個人執行任務一樣，我們越能以直接明瞭的方式說明我們想要什麼，Claude 的回應就越準確。

在我們最初的「糟糕」提示詞中，指示如下：

> I have this patient medical record. Can you summarize it for me?

這實在過於模糊！我們需要制定一套清楚、具體的指示。我們究竟想要什麼樣的摘要？

假設我們希望摘要包含以下幾個不同類別的資訊：

* 病人姓名
* 病人年齡
* 主要診斷清單
* 病人目前用藥清單
* 非藥物治療清單（物理治療、CBT 等）
* 近期關注事項清單
* 醫師的重要待辦事項清單

同時，指定我們想要的確切輸出格式也很重要，因此我們要確保請 Claude 使用條列式清單，而非泛泛的「清單」。

以下是更新後的提示詞版本：

```python
#System Prompt
system = """
You are a highly experienced medical professional with a specialty in translating complex patient histories into concise, actionable summaries. 
Your role is to analyze patient records, identify critical information, and present it in a clear, structured format that aids in diagnosis and treatment planning. 
Your summaries are invaluable for busy healthcare providers who need quick insights into a patient's medical history before appointments.
"""

#Improved Prompt (still a work in progress!)
updated_prompt = """
I need your help summarizing patient medical records for our team of doctors. 
We have a series of follow-up appointments tomorrow, and the doctors need quick, insightful summaries to prepare. 

Each summary should include the following elements in this order:
- The patient's name
- The patients age
- A bulleted list of key diagnoses in chronological order
- A bulleted list of medications the patient is prescribed
- A bulleted list of other treatments: non-medication treatments like CBT or physical therapy
- A short bulleted list of recent concerns
- A bulleted list of key action items to help our doctors prepare for the upcoming patient visit

<patient_record>
{record}
</patient_record>
"""
```


### 加入範例

範例是提升 Claude 表現、引導其產生期望輸出的最強大工具之一。透過在提示詞中提供幾個精心設計的範例，我們可以顯著提升 Claude 回應的準確性、一致性和品質。這項技巧對於高度細節化、需要結構化輸出或遵循特定格式的任務特別有效。

目前，我們的提示詞完全沒有包含任何範例。為了簡潔，我們只加入一個範例，雖然通常最好至少有兩個。

我們將以這份病歷作為範例輸入：

```
Patient Name: Ethan Blackwood
Age: 55
Medical Record:

2010: Annual check-up, mild hypertension noted
  - Started on lifestyle modifications (diet, exercise)
2012: Diagnosed with moderate depression following job loss
  - Started on sertraline and cognitive-behavioral therapy (CBT)
2014: New job, reported improved mood
  - Continued sertraline, reduced CBT sessions
2015: Mild back pain, diagnosed with early degenerative disc disease
  - Physical therapy and over-the-counter NSAIDs prescribed
2016: Hypertension worsened, started on lisinopril
2017: Routine colonoscopy showed benign polyps, removed during procedure
2018: Developed persistent cough, chest X-ray clear
  - Diagnosed with Gastroesophageal Reflux Disease (GERD)
  - Started on omeprazole
2019: Diagnosed with obstructive sleep apnea (OSA)
  - Started CPAP therapy, reported improved energy levels
2020: COVID-19 pandemic, worked from home
  - Reported increased anxiety, CBT sessions resumed (telehealth)
  - COVID-19 vaccination (Moderna, both doses)
2021: Mild knee pain, MRI showed minor meniscus tear
  - Arthroscopic surgery recommended, patient opted for conservative management
2022: Annual check-up showed pre-diabetes (A1C: 6.1%)
  - Intensified lifestyle modifications, referred to nutritionist
- Discontinued omeprazole due to resolved GERD symptoms
2023: Blood tests showed elevated PSA (Prostate-Specific Antigen)
  - Prostate biopsy performed, results negative for cancer
- Knee pain worsened, agreed to arthroscopic surgery
2024: Post-op knee recovery: good, continuing physical therapy
  - A1C levels improved (5.8%), pre-diabetes resolved
  - Stress test normal, but mild LVH on echocardiogram
  - Started on low-dose ACE inhibitor for cardioprotection
```

根據這個範例輸入，一份遵循提示詞規則、格式良好的輸出可能如下所示：

```
Name: Ethan Blackwood
Age: 55  

Key Diagnoses:
- Hypertension (2010)
- Depression (2012)
- Degenerative Disc Disease (2015) 
- Gastroesophageal Reflux Disease (GERD) (2018)
- Obstructive Sleep Apnea (OSA) (2019)
- Pre-diabetes (2022)
- Meniscus Tear (2021)
- Left Ventricular Hypertrophy (LVH) (2024)

Medications: 
- Sertraline (depression)
- Lisinopril (hypertension)
- Omeprazole (GERD) - discontinued in 2022
- Low-dose ACE inhibitor (cardioprotection - 2024)

Other Treatments:
- Cognitive Behavioral Therapy (CBT) (depression)
- Physical therapy (back pain, post-op knee recovery)
- CPAP therapy (OSA)
- Arthroscopic knee surgery (2023)

Recent Concerns:
- Worsening knee pain
- Elevated PSA (2023) 
- Left ventricular hypertrophy on echocardiogram (2024)

Action Items:  
- Follow up on post-op knee recovery and physical therapy  
- Monitor PSA levels and prostate health
- Optimize blood pressure and hypertension management
- Assess need for further cardiac workup after LVH finding

```

讓我們更新提示詞，加入這個範例輸入與輸出。為了讓 Claude 更清楚，我們會用 `<example>` 標籤包裹範例：

```python
#System Prompt
system = """
You are a highly experienced medical professional with a specialty in translating complex patient histories into concise, actionable summaries. 
Your role is to analyze patient records, identify critical information, and present it in a clear, structured format that aids in diagnosis and treatment planning. 
Your summaries are invaluable for busy healthcare providers who need quick insights into a patient's medical history before appointments.
"""

#Improved Prompt (still a work in progress!)
updated_prompt = """
I need your help summarizing patient medical records for our team of doctors. 
We have a series of follow-up appointments tomorrow, and the doctors need quick, insightful summaries to prepare. 

Each summary should include the following elements in this order:
- The patient's name
- The patients age
- A bulleted list of key diagnoses in chronological order
- A bulleted list of medications the patient is prescribed
- A bulleted list of other treatments: non-medication treatments like CBT or physical therapy
- A short bulleted list of recent concerns
- A bulleted list of key action items to help our doctors prepare for the upcoming patient visit

Here's an example of how we'd like the summaries formatted:

<example>
<patient_record>
Patient Name: Ethan Blackwood
Age: 55
Medical Record:

2010: Annual check-up, mild hypertension noted
  - Started on lifestyle modifications (diet, exercise)
2012: Diagnosed with moderate depression following job loss
  - Started on sertraline and cognitive-behavioral therapy (CBT)
2014: New job, reported improved mood
  - Continued sertraline, reduced CBT sessions
2015: Mild back pain, diagnosed with early degenerative disc disease
  - Physical therapy and over-the-counter NSAIDs prescribed
2016: Hypertension worsened, started on lisinopril
2017: Routine colonoscopy showed benign polyps, removed during procedure
2018: Developed persistent cough, chest X-ray clear
  - Diagnosed with Gastroesophageal Reflux Disease (GERD)
  - Started on omeprazole
2019: Diagnosed with obstructive sleep apnea (OSA)
  - Started CPAP therapy, reported improved energy levels
2020: COVID-19 pandemic, worked from home
  - Reported increased anxiety, CBT sessions resumed (telehealth)
  - COVID-19 vaccination (Moderna, both doses)
2021: Mild knee pain, MRI showed minor meniscus tear
  - Arthroscopic surgery recommended, patient opted for conservative management
2022: Annual check-up showed pre-diabetes (A1C: 6.1%)
  - Intensified lifestyle modifications, referred to nutritionist
- Discontinued omeprazole due to resolved GERD symptoms
2023: Blood tests showed elevated PSA (Prostate-Specific Antigen)
  - Prostate biopsy performed, results negative for cancer
- Knee pain worsened, agreed to arthroscopic surgery
2024: Post-op knee recovery: good, continuing physical therapy
  - A1C levels improved (5.8%), pre-diabetes resolved
  - Stress test normal, but mild LVH on echocardiogram
  - Started on low-dose ACE inhibitor for cardioprotection
</patient_record>


Your output: 

Name: Ethan Blackwood
Age: 55  

Key Diagnoses:
- Hypertension (2010)
- Depression (2012)
- Degenerative Disc Disease (2015) 
- Gastroesophageal Reflux Disease (GERD) (2018)
- Obstructive Sleep Apnea (OSA) (2019)
- Pre-diabetes (2022)
- Meniscus Tear (2021)
- Left Ventricular Hypertrophy (LVH) (2024)

Medications: 
- Sertraline (depression)
- Lisinopril (hypertension)
- Omeprazole (GERD) - discontinued in 2022
- Low-dose ACE inhibitor (cardioprotection - 2024)

Other Treatments:
- Cognitive Behavioral Therapy (CBT) (depression)
- Physical therapy (back pain, post-op knee recovery)
- CPAP therapy (OSA)
- Arthroscopic knee surgery (2023)

Recent Concerns:
- Worsening knee pain
- Elevated PSA (2023) 
- Left ventricular hypertrophy on echocardiogram (2024)

Action Items:  
- Follow up on post-op knee recovery and physical therapy  
- Monitor PSA levels and prostate health
- Optimize blood pressure and hypertension management
- Assess need for further cardiac workup after LVH finding
</example>

Now, please summarize the following patient record in the same format:
<patient_record>
{record}
</patient_record>
"""
```

### 輸出 XML 結構

一個常見的提示策略是請 Claude 在回應中使用 XML 標籤。這樣即使 Claude 決定加上「好的，以下是您請求的摘要！」之類的前言，或加入額外內容，我們也能更容易地提取我們真正需要的內容。

在這個情況下，讓 Claude 將病歷摘要生成在 `<summary>` 標籤內可能很有意義。一個簡單的實作方式是更新範例，向 Claude 展示我們想要的格式。

目前，提示詞中的範例部分如下所示：

```
Here's an example of how we'd like the summaries formatted:

<example>
<patient_record>
Patient Name: Ethan Blackwood
Age: 55
Medical Record:

2010: Annual check-up, mild hypertension noted
  - Started on lifestyle modifications (diet, exercise)
medical record truncated to keep the text short here...
</patient_record>

Your output: 

Name: Ethan Blackwood
Age: 55  

Key Diagnoses:
- Hypertension (2010)
summary truncated to keep the text short here...
</example>
```

只需一個簡單的變更，我們就能向 Claude 說明應將輸出包裹在 `<summary>` 標籤內：

```
Here's an example of how we'd like the summaries formatted:

<example>
<patient_record>
Patient Name: Ethan Blackwood
Age: 55
Medical Record:

2010: Annual check-up, mild hypertension noted
  - Started on lifestyle modifications (diet, exercise)
medical record truncated to keep the text short here...
</patient_record>

<summary>
Name: Ethan Blackwood
Age: 55  

Key Diagnoses:
- Hypertension (2010)
summary truncated to keep the text short here...
</summary>
</example>
```

讓我們更新提示詞的範例部分以反映這個變更：


```python
#System Prompt
system = """
You are a highly experienced medical professional with a specialty in translating complex patient histories into concise, actionable summaries. 
Your role is to analyze patient records, identify critical information, and present it in a clear, structured format that aids in diagnosis and treatment planning. 
Your summaries are invaluable for busy healthcare providers who need quick insights into a patient's medical history before appointments.
"""

#Improved Prompt (still a work in progress!)
updated_prompt = """
I need your help summarizing patient medical records for our team of doctors. 
We have a series of follow-up appointments tomorrow, and the doctors need quick, insightful summaries to prepare. 

Each summary should include the following elements in this order:
- The patient's name
- The patients age
- A bulleted list of key diagnoses in chronological order
- A bulleted list of medications the patient is prescribed
- A bulleted list of other treatments: non-medication treatments like CBT or physical therapy
- A short bulleted list of recent concerns
- A bulleted list of key action items to help our doctors prepare for the upcoming patient visit

Here's an example of how we'd like the summaries formatted:

<example>
<patient_record>
Patient Name: Ethan Blackwood
Age: 55
Medical Record:

2010: Annual check-up, mild hypertension noted
  - Started on lifestyle modifications (diet, exercise)
2012: Diagnosed with moderate depression following job loss
  - Started on sertraline and cognitive-behavioral therapy (CBT)
2014: New job, reported improved mood
  - Continued sertraline, reduced CBT sessions
2015: Mild back pain, diagnosed with early degenerative disc disease
  - Physical therapy and over-the-counter NSAIDs prescribed
2016: Hypertension worsened, started on lisinopril
2017: Routine colonoscopy showed benign polyps, removed during procedure
2018: Developed persistent cough, chest X-ray clear
  - Diagnosed with Gastroesophageal Reflux Disease (GERD)
  - Started on omeprazole
2019: Diagnosed with obstructive sleep apnea (OSA)
  - Started CPAP therapy, reported improved energy levels
2020: COVID-19 pandemic, worked from home
  - Reported increased anxiety, CBT sessions resumed (telehealth)
  - COVID-19 vaccination (Moderna, both doses)
2021: Mild knee pain, MRI showed minor meniscus tear
  - Arthroscopic surgery recommended, patient opted for conservative management
2022: Annual check-up showed pre-diabetes (A1C: 6.1%)
  - Intensified lifestyle modifications, referred to nutritionist
- Discontinued omeprazole due to resolved GERD symptoms
2023: Blood tests showed elevated PSA (Prostate-Specific Antigen)
  - Prostate biopsy performed, results negative for cancer
- Knee pain worsened, agreed to arthroscopic surgery
2024: Post-op knee recovery: good, continuing physical therapy
  - A1C levels improved (5.8%), pre-diabetes resolved
  - Stress test normal, but mild LVH on echocardiogram
  - Started on low-dose ACE inhibitor for cardioprotection
</patient_record>


<summary>
Name: Ethan Blackwood
Age: 55  

Key Diagnoses:
- Hypertension (2010)
- Depression (2012)
- Degenerative Disc Disease (2015) 
- Gastroesophageal Reflux Disease (GERD) (2018)
- Obstructive Sleep Apnea (OSA) (2019)
- Pre-diabetes (2022)
- Meniscus Tear (2021)
- Left Ventricular Hypertrophy (LVH) (2024)

Medications: 
- Sertraline (depression)
- Lisinopril (hypertension)
- Omeprazole (GERD) - discontinued in 2022
- Low-dose ACE inhibitor (cardioprotection - 2024)

Other Treatments:
- Cognitive Behavioral Therapy (CBT) (depression)
- Physical therapy (back pain, post-op knee recovery)
- CPAP therapy (OSA)
- Arthroscopic knee surgery (2023)

Recent Concerns:
- Worsening knee pain
- Elevated PSA (2023) 
- Left ventricular hypertrophy on echocardiogram (2024)

Action Items:  
- Follow up on post-op knee recovery and physical therapy  
- Monitor PSA levels and prostate health
- Optimize blood pressure and hypertension management
- Assess need for further cardiac workup after LVH finding
</summary>
</example>

Now, please summarize the following patient record in the same format:

<patient_record>
{record}
</patient_record>
"""
```

### 提示詞修改回顧
在測試新提示詞之前，先來回顧我們所做的變更：

* 加入了清楚的系統提示詞，設定情境並給予 Claude 明確的角色。
* 使用 XML 標籤結構化輸入資料，在我們的情況中使用 `<patient_record>`，讓提示詞中哪部分是輸入資料一目瞭然。
* 提供了清楚、具體的指示，說明摘要應涵蓋哪些重點，例如診斷、用藥和近期健康問題。
* 指定了摘要的期望格式。
* 加入了一個範例輸入及對應的格式良好摘要，引導 Claude 的回應。
* 請求 Claude 將摘要生成在 `<summary>` 標籤內。

---

## 測試新提示詞
讓我們用新的 `system` 和 `updated_prompt` 提示詞，對 `patient_records` 清單中相同的 5 份病歷進行測試：

```python
def generate_summary_with_improved_prompt(patient_record):
    prompt_with_record = updated_prompt.format(record=patient_record) #use our rewritten prompt!
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        system=system, #add in our system prompt!
        messages=[{"role": "user", "content": prompt_with_record}]
    )
    print("===============================")
    print(response.content[0].text)
```

```python
generate_summary_with_improved_prompt(patient_records[0])
```

```
===============================
<summary>
Name: Evelyn Thompson
Age: 78

Key Diagnoses:
- Type 2 Diabetes (1985)
- Hypertension (1992)
- Osteoarthritis (Hip and Knee Replacements in 1998 and 2017)
- Hypothyroidism (2000)
- Atrial Fibrillation (2005)
- Vitamin B12 Deficiency (2008)
- Transient Ischemic Attack (TIA) (2011)
- Breast Cancer (2013)
- Chronic Kidney Disease (CKD) Stage 3 (2015)
- Pneumonia (2018)
- Mild Cognitive Impairment (2019)
- Recurrent Urinary Tract Infections (UTIs) (2021)

Medications:
- Metformin (Diabetes)
- Lisinopril (Hypertension)
- Levothyroxine (Hypothyroidism)
- Warfarin (Atrial Fibrillation)
- Aspirin (Antiplatelet)
- Anastrozole (Breast Cancer Recurrence Prevention)
- Donepezil (Cognitive Impairment)
- Low-dose Prophylactic Antibiotics (Recurrent UTIs)

Other Treatments:
- Total Hip Replacement (1998)
- Cataract Surgery (2003)
- Vitamin B12 Injections (2008)
- Lumpectomy and Radiation (Breast Cancer, 2013)
- Total Knee Replacement (2017)
- Physical Therapy and Home Health Aide (2023)

Recent Concerns:
- Worsening Kidney Function (eGFR Decline in 2022)
- Declining Mobility (2023)

Action Items:
- Monitor Kidney Function and Adjust Medications as Needed
- Continue Physical Therapy and Home Health Support
- Evaluate for Cognitive Decline and Adjust Treatment Plan
- Address Mobility Issues and Fall Risk
- Ensure Adherence to Recommended Cancer Screening
</summary>
```

```python
generate_summary_with_improved_prompt(patient_records[1])
```

```
===============================
<summary>
Name: Marcus Reyes
Age: 42

Key Diagnoses:
- Generalized Anxiety Disorder (GAD) (2001)  
- Major Depressive Disorder (MDD) (2003)
- Attention-Deficit/Hyperactivity Disorder (ADHD) (2007)
- Obstructive Sleep Apnea (OSA) (2012)
- Hypertension (2014)
- Type 2 Diabetes (2016)
- Gastroesophageal Reflux Disease (GERD) (2019)
- Plantar Fasciitis (2021)

Medications:
- Paroxetine (GAD) - switched to escitalopram in 2009
- Bupropion (MDD) - switched to venlafaxine in 2018  
- Methylphenidate (ADHD)
- Losartan (hypertension)
- Metformin (diabetes)
- Insulin therapy (diabetes) - initiated in 2017
- Omeprazole (GERD)  
- Quetiapine (antipsychotic) (2023)
- Lamotrigine (mood stabilizer) (2023)

Other Treatments: 
- Cognitive Behavioral Therapy (CBT)
- Dialectical Behavior Therapy (DBT) (2020)
- CPAP therapy (OSA)
- Orthotics and physical therapy (plantar fasciitis)
- Inpatient psychiatric treatment (2023)

Recent Concerns:
- Suicide attempt (2023)  
- Panic attack (2022)
- Weight gain and poor diabetes control

Action Items:
- Monitor mental health closely, ensure compliance with new medication regimen
- Follow up on diabetes management, lifestyle modifications for weight loss  
- Continue CBT/DBT and evaluate need for increased therapy sessions
- Screen for potential medication side effects impacting sleep, weight, anxiety
</summary>
```

```python
generate_summary_with_improved_prompt(patient_records[2])
```

```
===============================
<summary>
Name: Lily Chen
Age: 8

Key Diagnoses:
- Tetralogy of Fallot (TOF) (2016 - Birth)
- Developmental Delay (2018)
- Failure to Thrive (2019)  
- Sensory Processing Disorder (SPD) (2020)
- Attention-Deficit/Hyperactivity Disorder (ADHD) (2022)
- Sensorineural Hearing Loss (2023)

Medications:
- Amiodarone (post-operative arrhythmias - 2017)

Other Treatments:
- Surgical Repair of TOF (2017)
- Early Intervention Services (2018) 
- Speech Therapy (2018 - ongoing)
- Occupational Therapy (2019 - 2024)  
- Integrated Preschool Program with IEP (2021)
- Behavioral Therapy for ADHD (2022)
- Cochlear Implant Surgery (2023)
- Mainstream School with IEP Support (2023 - ongoing)
- Balloon Valvuloplasty for Pulmonary Stenosis (2022)

Recent Concerns: 
- Progression of Pulmonary Stenosis requiring intervention (2022)
- Ongoing speech development delays

Action Items:
- Monitor cardiac status, pulmonary valve function
- Continue speech and language therapy  
- Assess need for ongoing ADHD treatment and IEP accommodations
- Ensure appropriate developmental support in mainstream education setting
</summary>
```

```python
generate_summary_with_improved_prompt(patient_records[3])
```

```
===============================
<summary>
Name: Jason Tran
Age: 25

Key Diagnoses:
- Asthma (2010)
- Concussions (2012, 2014)
- Post-Concussion Syndrome (2014)
- Depression and Anxiety (2015)
- ACL Tear (2016)
- PTSD (2018)
- Sleep Apnea (2021)

Medications:
- Albuterol inhaler (asthma)
- Fluoxetine (depression, anxiety)

Other Treatments:
- Cognitive Rehabilitation Therapy (post-concussion syndrome)
- Cognitive-Behavioral Therapy (CBT) (PTSD, anxiety)
- Exposure Therapy (PTSD)
- Mindfulness Meditation and Yoga (anxiety)
- CPAP Therapy (sleep apnea)
- Surgical Fixation (fractured tibia, 2013)
- ACL Reconstruction Surgery (2016)
- Physical Rehabilitation (post-ACL surgery)

Recent Concerns:
- Returning to sports and managing anxiety/PTSD
- Sleep quality and sleep apnea

Action Items:
- Monitor asthma control and medication adherence
- Continue CBT and exposure therapy for PTSD/anxiety
- Assess need for ongoing CPAP therapy for sleep apnea
- Encourage gradual return to low-impact sports and training
- Support youth concussion awareness efforts
</summary>
```

```python
generate_summary_with_improved_prompt(patient_records[4])
```

```
===============================
<summary>
Name: Amira Khan
Age: 36

Key Diagnoses:
- Fibromyalgia (2011)
- Cutaneous Lupus Erythematosus (CLE) (2012)
- Systemic Lupus Erythematosus (SLE) (2013)
- Lupus Nephritis (2014)
- Interstitial Lung Disease (ILD) (2015)
- Sjögren's Syndrome (2016)
- Lupus Cerebritis (2017)
- Avascular Necrosis (AVN) of Hip (2018)
- Steroid-induced Diabetes (2021)
- Diastolic Dysfunction (2023)

Medications:
- Pregabalin (fibromyalgia)
- Hydroxychloroquine (SLE)
- Prednisone (SLE)
- Mycophenolate Mofetil (lupus nephritis)
- Cyclophosphamide (ILD)
- Pilocarpine (Sjögren's syndrome)
- Rituximab (lupus cerebritis)
- Belimumab (reduce flare frequency)
- Metformin and Insulin (steroid-induced diabetes)
- Abatacept (SLE flare)
- ACE Inhibitors (diastolic dysfunction)

Other Treatments:
- Physical Therapy (fibromyalgia, joint health)
- Topical Corticosteroids and Sunscreen (CLE)
- Home Oxygen Therapy (ILD)
- Total Hip Replacement Surgery (AVN)
- Yoga (joint health)
- Cardio-rehab (diastolic dysfunction)

Recent Concerns:
- SLE Flare-up (2022)
- Early Diastolic Dysfunction (2023)
- Planning Pregnancy (2024)

Action Items:
- Optimize SLE management, monitor disease activity
- Continue tapering immunosuppressants with close monitoring
- Lifestyle modifications for diabetes and cardiac health  
- Evaluate fertility and pregnancy plans with high-risk OB
- Monitor for potential medication interactions or teratogenicity
</summary>
```

效果很好！每個輸出都遵循了我們指定的規則和格式。
回到頁面頂端，看看使用最初提示詞時 Claude 生成的輸出類型，並與我們新的一致性輸出進行比較！

---

## 換個方式：JSON！

我們或許對目前提示詞產生的文字摘要感到滿意，但通常我們想要更容易以程式化方式處理的特定結構化回應。最常見的方式是使用 JSON。

**注意：強制取得 JSON 回應最簡單的方法是透過 Claude 的工具使用功能，[我們在工具使用課程的獨立章節中有介紹](https://github.com/anthropics/courses/blob/master/tool_use/03_structured_outputs.ipynb)。本次示範的重點在於展示修改提示詞所能帶來的影響。**

為了調整目前的提示詞以生成 JSON 回應，我們需要做幾項修改：
* 明確告訴 Claude 我們想要 JSON 結果，並指定 JSON 輸出應包含哪些內容。
* 將範例摘要更新為 JSON 輸出。

```python
# Unchanged System Prompt
system = """
You are a highly experienced medical professional with a specialty in translating complex patient histories into concise, actionable summaries. 
Your role is to analyze patient records, identify critical information, and present it in a clear, structured format that aids in diagnosis and treatment planning. 
Your summaries are invaluable for busy healthcare providers who need quick insights into a patient's medical history before appointments.
"""

#Prompt updated to generate JSON
updated_json_prompt = """
I need your help summarizing patient medical records for our team of doctors.
We have a series of follow-up appointments tomorrow, and the doctors need quick, insightful summaries to prepare. 

Please provide these summaries in JSON format with the following structure:
{
  "name": "Patient's full name",
  "age": patient's age as an integer,
  "key_diagnoses": [
    {
      "diagnosis": "Primary diagnosis",
      "year": year of diagnosis as an integer
    },
    ...
  ],
  "medications": [
    {
      "name": "Medication name",
      "purpose": "Brief description of what it's for"
    },
    ...
  ],
  "other_treatments": [
    {
      "treatment": "Treatment name",
      "purpose": "Brief description of what it's for"
    },
    ...
  ],
  "recent_concerns": [
    "Brief statement of recent health issue or concern"
  ],
  "action_items": [
    "Action item 1",
    "Action item 2",
    ...
  ]
}

Here's an example of how we'd like the summaries formatted:

<example>
<patient_record>
Patient Name: Ethan Blackwood
Age: 55
Medical Record:

2010: Annual check-up, mild hypertension noted
  - Started on lifestyle modifications (diet, exercise)
2012: Diagnosed with moderate depression following job loss
  - Started on sertraline and cognitive-behavioral therapy (CBT)
2014: New job, reported improved mood
  - Continued sertraline, reduced CBT sessions
2015: Mild back pain, diagnosed with early degenerative disc disease
  - Physical therapy and over-the-counter NSAIDs prescribed
2016: Hypertension worsened, started on lisinopril
2017: Routine colonoscopy showed benign polyps, removed during procedure
2018: Developed persistent cough, chest X-ray clear
  - Diagnosed with Gastroesophageal Reflux Disease (GERD)
  - Started on omeprazole
2019: Diagnosed with obstructive sleep apnea (OSA)
  - Started CPAP therapy, reported improved energy levels
2020: COVID-19 pandemic, worked from home
  - Reported increased anxiety, CBT sessions resumed (telehealth)
  - COVID-19 vaccination (Moderna, both doses)
2021: Mild knee pain, MRI showed minor meniscus tear
  - Arthroscopic surgery recommended, patient opted for conservative management
2022: Annual check-up showed pre-diabetes (A1C: 6.1%)
  - Intensified lifestyle modifications, referred to nutritionist
- Discontinued omeprazole due to resolved GERD symptoms
2023: Blood tests showed elevated PSA (Prostate-Specific Antigen)
  - Prostate biopsy performed, results negative for cancer
- Knee pain worsened, agreed to arthroscopic surgery
2024: Post-op knee recovery: good, continuing physical therapy
  - A1C levels improved (5.8%), pre-diabetes resolved
  - Stress test normal, but mild LVH on echocardiogram
  - Started on low-dose ACE inhibitor for cardioprotection
</patient_record>


<summary>
{
  "name": "Ethan Blackwood",
  "age": 55,
  "key_diagnoses": [
    {
      "diagnosis": "Hypertension",
      "year": 2010
    },
    {
      "diagnosis": "Depression",
      "year": 2012
    },
    {
      "diagnosis": "Degenerative Disc Disease",
      "year": 2015
    },
    {
      "diagnosis": "Gastroesophageal Reflux Disease (GERD)",
      "year": 2018
    },
    {
      "diagnosis": "Obstructive Sleep Apnea (OSA)",
      "year": 2019
    },
    {
      "diagnosis": "Pre-diabetes",
      "year": 2022
    },
    {
      "diagnosis": "Left Ventricular Hypertrophy (LVH)",
      "year": 2024
    }
  ],
  "medications": [
    {
      "name": "Lisinopril",
      "purpose": "Hypertension management"
    },
    {
      "name": "Sertraline",
      "purpose": "Depression"
    },
    {
      "name": "ACE inhibitor (low-dose)",
      "purpose": "Cardioprotection"
    }
  ],
  "other_treatments": [
    {
      "treatment": "Cognitive Behavioral Therapy (CBT)",
      "purpose": "Depression management"
    },
    {
      "treatment": "Physical therapy",
      "purpose": "Back pain and knee recovery"
    },
    {
      "treatment": "CPAP therapy",
      "purpose": "Obstructive Sleep Apnea"
    },
    {
      "treatment": "Arthroscopic knee surgery",
      "purpose": "Meniscus tear repair"
    }
  ],
  "recent_concerns": [
    "Worsening knee pain, addressed with surgery",
    "Elevated PSA (2023), biopsy negative",
    "Mild left ventricular hypertrophy (2024)"
  ],
  "action_items": [
    "Follow up on post-op knee recovery and PT progress",
    "Monitor PSA levels and prostate health",
    "Assess cardiac health post-LVH finding",
    "Review blood pressure management"
  ]
}
</summary>
</example>

Now, please summarize the following patient record in the same format.  Output your JSON sumary inside of <summary> tags
"""

#Broke this part into its own variable to make it easier to use the `format` method later
# (the JSON curly braces in the above prompt variable cause problems when using `format` )
medical_record_input_prompt = """
<patient_record>
{record}
</patient_record>
"""
```

讓我們用以下函式來測試：

```python
def generate_summary_with_json_prompt(patient_record):
    final_prompt_part = medical_record_input_prompt.format(record=patient_record) #add the medical record to the final prompt piece
    complete_prompt = updated_json_prompt + final_prompt_part
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        system=system, #add in our system prompt!
        messages=[{"role": "user", "content": complete_prompt}]
    )
    print(response.content[0].text)
```

```python
generate_summary_with_json_prompt(patient_records[0])
```

```
<summary>
{
  "name": "Evelyn Thompson",
  "age": 78,
  "key_diagnoses": [
    {
      "diagnosis": "Type 2 Diabetes",
      "year": 1985
    },
    {
      "diagnosis": "Hypertension",
      "year": 1992
    },
    {
      "diagnosis": "Osteoarthritis",
      "year": 1998
    },
    {
      "diagnosis": "Hypothyroidism",
      "year": 2000
    },
    {
      "diagnosis": "Atrial Fibrillation",
      "year": 2005
    },
    {
      "diagnosis": "Vitamin B12 Deficiency",
      "year": 2008
    },
    {
      "diagnosis": "Transient Ischemic Attack (TIA)",
      "year": 2011
    },
    {
      "diagnosis": "Breast Cancer (Stage 2)",
      "year": 2013
    },
    {
      "diagnosis": "Chronic Kidney Disease (CKD Stage 3)",
      "year": 2015
    },
    {
      "diagnosis": "Mild Cognitive Impairment",
      "year": 2019
    }
  ],
  "medications": [
    {
      "name": "Metformin",
      "purpose": "Diabetes management"
    },
    {
      "name": "Lisinopril",
      "purpose": "Hypertension management"
    },
    {
      "name": "Levothyroxine",
      "purpose": "Hypothyroidism treatment"
    },
    {
      "name": "Warfarin",
      "purpose": "Anticoagulant for atrial fibrillation"
    },
    {
      "name": "Vitamin B12 Injections",
      "purpose": "B12 deficiency treatment"
    },
    {
      "name": "Aspirin",
      "purpose": "Antiplatelet therapy after TIA"
    },
    {
      "name": "Anastrozole",
      "purpose": "Breast cancer recurrence prevention"
    },
    {
      "name": "Donepezil",
      "purpose": "Treatment for mild cognitive impairment"
    },
    {
      "name": "Prophylactic Antibiotics",
      "purpose": "Prevention of recurrent UTIs"
    }
  ],
  "other_treatments": [
    {
      "treatment": "Total Hip Replacement",
      "purpose": "Osteoarthritis management"
    },
    {
      "treatment": "Cataract Surgery",
      "purpose": "Vision improvement"
    },
    {
      "treatment": "Lumpectomy and Radiation",
      "purpose": "Breast cancer treatment"
    },
    {
      "treatment": "Total Knee Replacement",
      "purpose": "Osteoarthritis management"
    },
    {
      "treatment": "IV Antibiotics",
      "purpose": "Treatment for pneumonia"
    },
    {
      "treatment": "Physical Therapy",
      "purpose": "Mobility and functional improvement"
    },
    {
      "treatment": "Home Health Aide",
      "purpose": "Assistance with activities of daily living"
    }
  ],
  "recent_concerns": [
    "Declining mobility and functional status",
    "Worsening kidney function (eGFR)",
    "Recurrent urinary tract infections (UTIs)"
  ],
  "action_items": [
    "Review diabetes and hypertension management",
    "Monitor kidney function and adjust medications as needed",
    "Optimize mobility and functional status through PT and home care",
    "Assess cognitive status and efficacy of donepezil",
    "Evaluate risk for falls and need for additional safety measures"
  ]
}
</summary>
```

我們成功取得想要的 JSON 格式了！
為了展示新的 JSON 回應有多容易處理，讓我們撰寫一個函式，為一批病人生成摘要，然後輸出特定醫師一天門診中可能需要的所有「待辦事項」清單：

```python
import re
import json

def generate_summary_with_json_prompt(patient_record):
    final_prompt_part = medical_record_input_prompt.format(record=patient_record) #add the medical record to the final prompt piece
    complete_prompt = updated_json_prompt + final_prompt_part
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        system=system, #add in our system prompt!
        messages=[{"role": "user", "content": complete_prompt}]
    )
    return response.content[0].text

def extract_json_from_summary_tags(summary_string):
     # Use regular expressions to find content between <summary> tags
    match = re.search(r'<summary>\s*(.*?)\s*</summary>', summary_string, re.DOTALL)
    if not match:
        print("No <summary> tags found in the input string.")
        return

    # Extract the JSON string
    return  match.group(1)

def extract_action_items(model_response):
    summary = extract_json_from_summary_tags(model_response)
    try:
        # Parse the JSON string
        summary_data = json.loads(summary)

        # Extract and print action items
        action_items = summary_data.get('action_items', [])
        patient_name = summary_data.get('name', "")
        print(f"Action Items for {patient_name}:")
        for idx, item in enumerate(action_items, 1):
            print(f"{idx}. {item}")
    except json.JSONDecodeError:
        print("Failed to parse JSON. Make sure the content between <summary> tags is valid JSON.")

def generate_daily_action_items(patient_records):
    # Takes a list of patient records, generates a summary for each, and prints the action items:
    for record in patient_records:
        summary = generate_summary_with_json_prompt(record)
        extract_action_items(summary)
```

```python
generate_daily_action_items(patient_records)
```

```
Action Items for Evelyn Thompson:
1. Monitor kidney function and adjust medications as needed
2. Evaluate cognitive status and optimize treatment
3. Assess mobility and home safety, consider assistive devices
4. Follow up on breast cancer surveillance and prevention
Action Items for Marcus Reyes:
1. Monitor mental health closely, ensure adequate support system
2. Evaluate effectiveness of updated medication regimen
3. Continue lifestyle and diabetes management (diet, exercise)
4. Follow-up physical therapy for plantar fasciitis
5. Provide resources for patient and family related to mental health
Action Items for Lily Chen:
1. Evaluate current educational and therapy needs
2. Monitor hearing and speech progress post-cochlear implant
3. Assess cardiac status and need for future interventions
4. Continue close developmental monitoring and support
Action Items for Jason Tran:
1. Monitor asthma control and medication adherence
2. Assess mental health status and therapy progress
3. Evaluate sleep quality and CPAP compliance
4. Encourage gradual return to low-impact sports
5. Discuss potential for sports-related head injuries
Action Items for Amira Khan:
1. Monitor organ system involvement and adjust treatments
2. Manage steroid-induced diabetes and cardiovascular risk factors
3. Provide pre-conception counseling and coordinate high-risk OB care
4. Optimize physical therapy and lifestyle modifications
```

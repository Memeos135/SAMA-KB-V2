# SAMA_EN_11076_VER1.pdf

## Page 1

السادة/ المحترمون
السلام عليكم ورحمة الله وبركاته.
الموضوع: توحيد معايير إيصالات أجهزة الصرف الآلي.

استنادًا إلى الصلاحيات المنوطة بالبنك المركزي السعودي بموجب نظامه الصادر بالمرسوم الملكي
رقم (م/37) وتاريخ ١١/47/5١ه؛‏ ونظام مراقبة البنوك الصادر بالمرسوم ‎SLM‏ رقم (م/ه)
وتاريخ 7831/1/77 فى وإشارةً إلى اتفاقية مستوى خدمة أجهزة الصرف الآلي (الإصدار الثاني) الصادرة
بموجب تعميم البنك المركزي رقم (41977/777) وتاريخ ‎51/7/١١‏ ١ه‏ واستمرارًا للجهود المبذولة في تطوير
البنى التحتية لنظم المدفوعات في المملكة.

مرافق لكم مبادرة إيصالات أجهزة الصرف الآلي ‎(Requirements for ATM Receipts Initiative)‏
الصادرة عن المدفوعات السعودية. والتي يتعين على البنوك تنفيذها على أجهزة الصرف الآلي. حيث تهدف
المبادرة إلى تقليص طلبات العملاء للإيصالات الورقية في معاملات أجهزة الصرف ‎TY)‏ وذلك من خلال توحيد
سير عمل الشاشات عبر جميع الأجهزة لضمان تحقيق الآتي:

- الحفاظ على البيئة ‎billy‏ العام.

- توحيد تجربة المستخدم عبر جميع أجهزة الصرف الآلي.

عليه؛ يؤكد البنك المركزي على كافة البنوك والمصارف العاملة في المملكة والأعضاء في شبكة المدفوعات
السعودية الالتزام والتقيد بما ورد في المبادرة المرافقة. ويمكن التنسيق في هذا الشأن مع المختصين في
المدفوعات السعودية عبر البريد الإلكتروني ‎(onboarding@saudipayments.com)‏

‎x‏ وتقبلوا تحياتي.
5“ 7

‏فهد بن إبراهيم ‎GAB‏
‏وكيل المحافظ للرقابة
عنه / زياد بن بندر اليوسف
وكيل المحافظ للتطوير والتقنية

‏نطاق التوزيع:
البنوك والمصارف العاملة في المملكة.
ار 3
المدفوعات السعودية.

## Page 2

المدفوعات السعودية
‎SAUDI PAYMENTS‏

Requirements for ATM Receipts Initiative

November 2021

## Page 3

Public

Requirements for ATM Receipts Initiative November 2021
Table of Contents
1. INTRODUCTION 3
1.1 Purpose OF DOCUMENT
1.2 Scope OF DOCUMENT
1.3 AUDIENCE OF DOCUMENT
2. OVERVIEW 4
3. NEW ATM SCREEN WORKFLOWS 5
3.1 CASH WITHDRAWAL TRANSACTION STREAM
3.2 NON-CASH TRANSACTIONS STREAM
4. APPENDIX 7

4.1 WoRKFLOWS FOR CASH WITHDRAWAL TRANSACTIONS STREAM

4.1.1 WORKFLOW FOR CASH WITHDRAWAL (WITHOUT RECEIPT)

4.1.2 WORKFLOW FOR CASH WITHDRAWAL WITH RECEIPT

4.2 WORKFLOWS FOR NON-CASH TRANSACTIONS STREAM

4.2.1 WORKFLOW FOR BALANCE ENQUIRY
4.2.2 WORKFLOW FOR MINI STATEMENT

4.2.3 WORKFLOW FOR CASH DEPOSIT

Page |2

10

10

11

12

## Page 4

Public
Requirements for ATM Receipts Initiative November 2021

1. Introduction

In line with SAMA’s and Saudi Payments’ vision to make continuous improvements in payment
infrastructure of the Kingdom, ATM Receipts initiative aims to minimize Cardholders’ dependency on
paper receipts for ATM transactions.
The sole objectives of this initiative are to:

v Enable cost efficiency for Acquirers

v Maximize customer data privacy and protection

vy Save environment and go green!

1.1 Purpose of Document

The purpose of this document is to assign rules and requirements related to ATM Receipts to external
stakeholders who play significant roles in the success of this change. This document is intended to govern
the responsibilities of mada Members from multiple aspects for the purpose of ensuring the quality of the

solution.

1.2 Scope of Document

This document covers the rules and requirements for ATM Receipts initiative. It also contains detailed
workflows of the new enhancements on ATM screens. This document, however, does not contain

certification procedures nor terms and conditions.

1.3 Audience of Document

The intended audience of this document is mada Members who are familiar with the basic guidelines of

ATM functionalities, and who must comply with these rules at all times.

Page | 3

## Page 5

Public
Requirements for ATM Receipts Initiative November 2021

2. Overview

ATM Receipts is an enhancement initiative that drives the market to minimize dependency on receipts for

the four (4) most commonly performed transactions on ATMs.

This initiative focusses on improving and unifying the screen workflow across all ATMs (off-us and on-us)
in an attempt to unify user experience and reduce demand on receipts as a result. However, paper receipts

shall still be available and provided to Cardholders whenever requested.

Currently, the Home page on ATMs —after inserting the card and entering the PIN— displays the four major
transactions (Cash Withdrawal, Balance Inquiry, Mini Statement, and Cash Deposit if available).

As part of this initiative, the Home page will be limited to whatever is available of those four transactions
and must be fixed and unified across all ATMs (including on-us and off-us). In addition to the four
transactions, the Home page also provides an ‘Others’ option which opens up to any other transaction(s)

and/or service(s) (i.e. PIN Change, Transfer...etc.).

The new enhancement on ATM screen flow runs into two streams: (1) Cash Withdrawal transaction stream,
and (2) ‘Non-cash transactions stream. Each of which has its own mechanism to achieve the same goal of

receipt reduction.

“Non-cash transactions include (1) Balance Enquiry, (2) Mini Statement, and (3) Cash Deposit —which is

currently available for on-us only.

Page |4

## Page 6

Public
Requirements for ATM Receipts Initiative November 2021

3. New ATM Screen Workflows

3.1 Cash Withdrawal Transaction Stream
Since Cash Withdrawal is the top transaction in terms of initiation and receipt requests, there will be two
separate transactions for Cash Withdrawal:
(1) The first transaction is “Cash Withdrawal” which is presented within the Home page on the ATM. This
transaction should not provide a receipt upon completion.
(2) The second transaction is “Cash Withdrawal with Receipt” which will be added inside the ‘Others’ page

from the Home page. This transaction should provide a receipt upon completion.

More importantly, after choosing either of the two transactions, if Cardholder selects one of the listed
amounts on the screen, card and cash should be collected immediately and without displaying the account
balance. However, in case Cardholder chooses “Another amount” and manually enters the amount, an
option to “Confirm and Display Balance” will be given to the Cardholder in addition to the default

option(s). The new workflow for Cash withdrawal transactions will be as follows:

Insert ‏و‎ Enter
card PIN
Amount Collectcard Collect cash
+ ,
| selected (balance is not displayed) (with receipt if chosen)
“Select transaction “Selectamount i 4
3
-50 -100 =
i—J
- Cash Withdrawal 3
-500 - 1000 3
‏عو‎
‎- Others: -Another - 5000
Cash Withdrawal SAUL 2 | ‏في‎
‎with Receipt Your new balance is
SAR
ia —— — >
“Another 3 SAR
amount” - Confirm ps &
a5
“Select transaction: This screen does not provide full content, as - Adjust 3 a
it is an illustration for the purpose of describing the stream only - Confirm and Display 3 ® Please oy dit
Ooo
*Select amount: This screen does not provide accurate content Balance 3 =

Amounts may vary.

A detailed workflow for the Cash Withdrawal transactions stream can be found in the Appendix.

Page |5

## Page 7

Public
Requirements for ATM Receipts Initiative November 2021

3.2 Non-cash Transactions Stream
As mentioned earlier, non-cash transactions include Balance Enquiry, Mini Statement, and Cash Deposit.
There will be two changes (or additions) to enhance the screen flow and reduce receipt demand for this
stream:
First, upon choosing Balance Enquiry or Mini Statement, the account balance or mini statement,
respectively, will be shown on the screen. And upon choosing Cash Deposit, the deposited amount as well
as the new balance will be shown on the screen.
Second, at the end of either of the three transactions, a receipt will not be automatically printed. However,
an option to “collect a receipt and exit” will be given to the Cardholder in addition to the default option(s)
— if chosen, the process should be ended and the card should be collected along with the receipt.
The new workflow for the non-cash transactions will be as follows:

Insert ‏و‎ Enter
card PIN |

Your balance/statement/deposit

Select transaction™ amountis
No
‏عاو لوي‎ ٍ Collect card
- Balance Enquiry Fant ReceiptandExit (with receipt if chosen)
— —~ ‏تمه‎

- Mini Statement

Would you like another

-C
asn Deposit transaction?

0 -Yes

-No

- Would like to collect a receipt
Yes and exit

“Select transaction: This screen does not provide full content, as it is an illustration for the purpose of describing the stream only.

A detailed workflow for the non-cash transactions stream can be found in the Appendix.

Page | 6

## Page 8

Public
Requirements for ATM Receipts Initiative November 2021

4. Appendix
4.1 Workflows for Cash Withdrawal Transactions Stream

4.1.1 Workflow for Cash Withdrawal (without receipt)

Please insert your card ‏الرجاء إدخال البطاقة‎

s

Please enter your PIN ‏الرجاء إدخال الرقم السري‎

a

Please select a transaction ‏الرجاء اختيار العملية‎

> Cash Withdrawal ‏سحب نقدي‎

> Cash Deposit glia ‏إيداع‎ (if available)
‏ع‎ Balance Enquiry ‏الرصيد‎ yc ‏استعلام‎
‎>» Mini Statement ‏كشف حساب مختصر‎
> Others mpi

This screen should be limited to these four transactions, along with “Others” option. Any additional transaction or

se

Please select an amount ‏الرجاء اختيار المبلغ‎

service must be added in the “Others” page.

> 50 > 100
> 500 > 0
>» 5000 > Other j5/ glo

1. If cardholder selects an amount, card and cash must be collected without displaying balance

2. This diagram is for illustration purposes. Amounts in reality may vary

s

Please enter an amount ‏الرجاء إدخال المبلغ‎

SAR

>» Confirm ‏تأكيد‎

> Adjust ‏تصحيح‎
‎> Confirm and Display Balance ‏تأكيد مع إظهار الرصيد‎

If cardholder chooses “Adjust”, amount should be emptied to be entered again.

Page |7

## Page 9

Public
Requirements for ATM Receipts Initiative November 2021
- Confirm- - Confirm and Display Balance -
- ‏تأكيد مع إظهار الرصيد - - تأكيد‎ -
Thank you , - ;
‏شكرا ال‎ Thank you ‏شكرا‎
‎Please collect your card ‏الرجاء استلام البطاقة‎ Your new balance is ‏رصيدك الجديد هو‎
SAR
Please collect your card ‏الرجاء استلام البطاقة‎

4.1.2 Workflow for Cash Withdrawal with Receipt

Please insert your card ‏الرجاء إدخال البطاقة‎

s

Please enter your PIN Wj! ‏الرجاء إدخال الرقم‎

+.

Please select a transaction ‏الرجاء اختيار العملية‎

Vv

Cash Withdrawal ‏سحب نقدي‎

> Cash Deposit glia ¢laul (if available)
>» Balance Enquiry ‏الرصيد‎ yc ‏استعلام‎
‎>» Mini Statement ‏كشف حساب مختصر‎
> Others ‏أخرى‎

This screen should be limited to these four transactions, along with “Others” option. Any additional transaction or

s

Please select a transaction ‏الرجاء اختيار العملية‎

service must be added in the “Others” page

سحب نقدي مع إيصال ‎Cash Withdrawal with Receipt‏ >
تغيير الرقم السري ‎PIN Change‏ >

This screen must include these two transactions as a minimum. More transactions/services may be added

s

Page |8

## Page 10

Public

Requirements for ATM Receipts Initiative November 2021

Please select an amount glial! ‏الرجاء اختيار‎

> 50 » 100

> 500 » 1000

>» 5000 > Other j5/ alia
1. If cardholder selects an amount, card and cash must be collected without displaying balance

2. This diagram is for illustration purposes. Amounts in reality may vary.

*

Please enter an amount ‏الرجاء إدخال المبلغ‎

SAR

> Confirm ‏تأكيد‎
‎> Adjust anni
> Confirm and Display Balance ‏تأكيد مع إظهار الرصيد‎

If cardholder chooses “Adjust”, amount should be emptied to be entered again

B

- Confirm- - Confirm and Display Balance -
+ ajalt- - ‏تأكيد مع إظهار الرصيد‎ -
Thank you , . .
‏شكرا الا‎ Thank you ‏شكرا‎
‎Please collect your card and receipt Your new balance is ‏رصيدك الجديد هو‎
‏الرجاء استلام البطاقة والإيصال‎ SAR

Please collect your card and receipt
‏الرجاء استلام البطاقة والإيصال‎

89

## Page 11

Public
Requirements for ATM Receipts Initiative November 2021

4.2 Workflows for Non-cash Transactions Stream

4.2.1 Workflow for Balance Enquiry

Please insert your card ‏الرجاء إدخال البطاقة‎

2

Please enter your PIN ‏الرجاء إدخال الرقم السري‎

es

Please select a transaction ‏الرجاء اختيار العملية‎

> Cash Withdrawal Wadi ‏سحب‎ (if available)
>» Cash Deposit (if available)

استعلام عن الرصيد ‎Balance Enquiry‏ >

كشف حساب مختصر ‎Mini Statement‏ >

> Others ‏أخرى‎

This screen should be limited to these four transactions only, along with the “Others” option. Any additional

transaction or service must be added in the “Others” page

s

Your balance is ‏هو‎ Clan)

SAR

Would you like another transaction? ‏هل ترغب بعملية أخرف؟‎

7 Yes ‏نعم‎
‎> Now

» Would like to collect a receipt and exit ‏أرغب باستلام الإيصال والخروج‎

If cardholder chooses “Yes”, the home page should be displayed as per the normal process.

s

-No- - Would like to collect a receipt and exit —
‏أرغب باستلام الإيصال والخروج - - لا-‎ -
Thank you ‏شكرا‎ Thank you ‏شكرا‎
‎Please collect your card Please collect your card and receipt
‏الرجاء استلام البطاقة والإيصال الرجاء استلام البطاقة‎

Page 0

## Page 12

Requirements for ATM Receipts Initiative

4.2.2 Workflow for Mini Statement

November 2021

Please insert your card ‏الرجاء إدخال البطاقة‎

s

Please enter your PIN ‏الرجاء إدخال الرقم السري‎

»

> Others nypl

This screen should be limited to these four transactions »

service must be added in the “Others” page

Please select a transaction ‏الرجاء اختيار العملية‎

> Cash Withdrawal Wadi ‏سحب‎ (if available)
>» Cash Deposit (if available)

استعلام عن الرصيد ‎Balance Enquiry‏ »>
كشف حساب مختصر ‎Mini Statement‏ >

nly, a

ong with the “Others” option. Any additional trans

s

7 Yes ‏نعم‎
‎> Now

Your mini statement is ‏كشف حسابك المختصر هو‎

Would you like another transaction?$unjsl ‏ترغب بعملية‎ Ja

If cardholder chooses “Yes”, the home page should be displayed as per the normal process.

> Would like to collect a receipt and exit ‏أرغب باستلام الإيصال والخروج‎ '

*

- فللا >
لا

Thank you sit

Please collect your card
‏الرجاء استلام البطاقة‎

- Would like to collect a receipt and exit —
- ‏أرغب باستلام الإيصال والخروج‎ -
Thank you ‏شكرا‎

Please collect your card and receipt
‏الرجاء استلام البطاقة والإيصال‎

Page |11

## Page 13

Public
Requirements for ATM Receipts Initiative November 2021

4.2.3 Workflow for Cash Deposit

Please insert your card ‏الرجاء إدخال البطاقة‎

s

Please enter your PIN ‏الرجاء إدخال الرقم الشسري‎

D2

Please select a transaction ‏الرجاء اختيار العملية‎

> Cash Withdrawal Wadi ‏سحب‎ (if available)
» Cash Deposit ‏مبلغ‎ clas!

> Balance Enquiry ‏الرصيد‎ yc ‏استعلام‎

كشف حساب مختصر ‎Mini Statement‏ >

> Others mpi

This screen should be limited to these four transactions only, along with the “Others” option. Any additional

transaction or service must be added in the “Others” page

=e

The deposited amount isga ‏الإيداع‎ glia
SAR

Your new balance is ‏رصيدك الجديد هو‎
SAR

Would you like another transaction? ‏ترغب بعملية أخرى؟‎ Ja

ry Yes ‏نعم‎
‎7 Nol

» Would like to collect a receipt and exit ‏أرغب باستلام الإيصال والخروج‎

If cardholder chooses “Yes”, the home page should be displayed as per the normal process

-No- - Would like to collect a receipt and exit —
“al - ‏أرغب باستلام الإيصال والخروج‎ -
Thank you ‏شكرا‎ Thank you ‏شكرا‎
‎Please collect your card Please collect your card and receipt
‏الرجاء استلام البطاقة والإيصال الرجاء استلام البطاقة‎

Page | 12

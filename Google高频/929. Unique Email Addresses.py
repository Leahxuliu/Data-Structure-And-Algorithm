# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/09  

'''
["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

题意：
1. @后面的.不能忽略
2. @前面的.忽略，+后面省略

Steps:
1. create a unique_email list to store email id
2. split email by @, local_name = email[0], domain[1]
3. split local_name by '.' and '+'
    choose the real name
4. put the real name into unique_email
5. count the len of unique_email
'''

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if len(emails) == 0:
            return 0
        
        res = set()
        for i in emails:
            local_name = i.split('@')[0]
            domain_name = i.split('@')[1]

            real_name = ''.join(local_name.split('+')[0].split('.'))
            res.add(real_name + '@' + domain_name)
        return len(res)
        

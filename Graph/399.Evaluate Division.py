#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/18  
# @Author  : XU Liu
# @FileName: 399.Evaluate Division.py

'''
1. 题目要求：
谷歌近6个月出了8次

2. 理解：
a/b = 2, b/c =3
相当于
a --> b --> c
  2倍    3倍
so a --> c 是6倍

a <-- b <-- c
  1/2倍   1/3倍

如果除数或者被除数不存在 --> -1.0
自己除自己 --> 1.0

3. 题目类型：
有向图，路径

4. 输出输入以及边界条件：
input: equations: List[List[str]], values: List[float], queries: List[List[str]]
output: values: List[float]
corner case: None

5. 解题思路
    

'''
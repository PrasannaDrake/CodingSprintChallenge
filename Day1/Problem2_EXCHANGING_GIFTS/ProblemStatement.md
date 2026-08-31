# Christmas Gift Exchange Problem - Identify Youngest Member

## Problem Statement 
The royal family exchanges gifts during Christmas following a specific custom. Among all family members, there is a **youngest member** who:
1. *Receives a gift from every other family member.*
2. *Does not give a gift to anyone.*

Given the total number of family members $n$ and a list of $m$ gift exchanges among them, your task is to identify the youngest member.

> **Note:** A family member does not give more than one gift to the same member (no duplicate edges).

## Core Logic
This problem can be modeled as ***Directed Graph*** where:   
      - Each family member represents a node (vertex) in the graph.  
      - Each gift exchange $a_i \rightarrow b_i$ represents a directed edge from node $a_i$ to node $b_i$.  
In graph theory termilogy, the youngest member is a **Universal Sink**:   
      - **Out-degree = 0**: The node has no outgoing edges (gives zero gifts.)  
      - **In-degree = n-1**: The node has incoming edge from every other node (receives gifts from all other n-1 members).  

## Algorithm Steps
1. Maintain two arrays/lists: in_degree and out_degree of size $n + 1$ (initialized to 0).
2. For each gift pair $(a_i, b_i)$:
      - Increment out_degree[a_i] by 1.
      - Increment in_degree[b_i] by 1.
3. Iterate through all members from 1 to n:  
      - If out_degree[i] == 0 and in_degree[i] == n -1, return i.
4. If loop finishes without finding such a candidate, return -1.
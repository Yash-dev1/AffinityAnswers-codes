A. How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger?

Ans - 8 types of tigers, ncbi_id = 9695
-------------------------------------------------------------------------------------------------------
B. Find all the columns that can be used to connect the tables in the given database.

Ans - 11 number of columns used as foregin key for the whole database. These columns are listed as:
1. rfam_acc
2. auto_overlap
3. clan_acc
4. pmid
5. auto_wiki
6. ncbi_id
7. rfamseq_acc
8. motif_acc
9. pdb_id
10. pdb_seq
11. refseq_acc
---------------------------------------------------------------------------------------------------------
C. Which type of rice has the longest DNA sequence? 
Ans - Oryza sativa Indica group, ncbi_id = 39946

----------------------------------------------------------------------------------------------------------
D. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page.
Ans - The query is wirtten as:
select rfam_acc,rfam_id,max(length) from (select rfam_acc,rfamseq_acc  from full_region) as b 
join (select rfamseq_acc,length  from rfamseq) as a on b.rfamseq_acc = a.rfamseq_acc group by b.rfam_acc
order by max(length) desc
limit 120,15; # limit clause for finding the 9th page

---------------------------------------------------X---------------------------------------------------------------------
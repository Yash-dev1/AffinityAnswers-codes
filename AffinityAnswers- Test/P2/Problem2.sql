Use Rfam;
# Q1
select count(distinct(species)) from taxonomy where species like "Panthera tigris%";
select ncbi_id from taxonomy where species like "Panthera tigris sumatrae%";

# Q2
SELECT 
    count(distinct(COLUMN_NAME)) FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    REFERENCED_TABLE_NAME IS NOT NULL
    AND TABLE_SCHEMA = 'Rfam';
    
# Q3
Select ncbi_id,sum(length) as l1 from rfamseq where ncbi_id in (Select ncbi_id from taxonomy where species like "Oryza sativa%")
group by ncbi_id order by l1 desc; # returns maximmu value for species no. 39946
Select species from taxonomy where ncbi_id = 39946;

# Q4
select rfam_acc,rfam_id,max(length) from (select rfam_acc,rfamseq_acc  from full_region) as b 
join (select rfamseq_acc,length  from rfamseq) as a on b.rfamseq_acc = a.rfamseq_acc group by b.rfam_acc
order by max(length) desc
limit 120,15; # limit clause for finding the 9th page


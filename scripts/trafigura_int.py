#

def find_missing_duplicate(input_list):
    missing_num = None
    duplicate_num = None
    input_list.sort()
    prev_num= 0
    diff = None
    # for index,value in enumerate(input_list, start=1):
    for value in input_list:

        diff = value - prev_num

        if diff==0:
            duplicate_num = value

        if diff>1:
            missing_num = prev_num+1

        prev_num=value

    return missing_num, duplicate_num



# input_list = [2,3,4,5,6,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
input_list = [1,2,3,4,5,6,7,8,9,9,10,11,12,13,14,15,16,17,19,20]
# input_list = [2,3,4,5,6,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# input_list = [1,3,3]

# input_list = [1,1,3]
# input_list = [2,3,4,5,6,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
missing_num, duplicate_num = find_missing_duplicate(input_list)
print(missing_num, duplicate_num)


# FLIGHTS
# flight_id, source,destination, dept_time ,arr_time
#
# SELECT flight_id
# FROM flights
# where source='Mumbai' and destination='Chennai'
# and DATE(dept_time) ='20220725'
#
# with temp1 as (
#     SELECT * FROM flights
#     where source='Mumbai'
# )
#
# with temp2 as (
#         SELECT * FROM flights
#         where destination='Chennai'
# )
#
# SELECT distinct(flight_id)
# FROM
# temp 1 as t1
# union
# temp2 as t2
# where datediff(t2.dept_time, t1.arr_time, 'h') <=3
# and t1.destination = t2.source
#
#
#
#
# # SELECT * FROM (
# #     SELECT flight_id, dense_rank() over (partition by flight_id order by flight_id) as count
# # )temp1
# # group by temp1flight_id
# # having count(temp1.count)> 1
#
# date+airline+
# flight_name
#
# username, query, query_id, text, date, table_name
#
# username, table, count_of_queries_table
#
# select username, table_name, count(query_id)
# from queries
# group by username, table_name
#
#
#
# SELECT flight_id,flight_name, count(*) as flight_count FROM flights
# group by flight_id, flight_name
# having flight_count > 1
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

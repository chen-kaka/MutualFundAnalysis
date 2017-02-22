
晨星基金排名指数计算SQL:

根据三年夏普比例排序的五星级基金
SELECT * FROM mutualfund.Model_mutualfundrating where StarRating3=5 and StarRating5=5 order by SR3Year desc, DR3Year asc;
根据三年晨星风险系数排序的五星级基金
SELECT * FROM mutualfund.Model_mutualfundrating where StarRating3=5 and StarRating5=5 order by DR3Year asc, SR3Year desc;

根据三年波动幅度最低排序的基金:
SELECT * FROM mutualfund.Model_mutualfundrating where SD3Year>0 order by SD3Year asc;

根据今年总汇报率最高排序的基金:
SELECT * FROM mutualfund.Model_mutualfundrating where ReturnYTD>0 order by ReturnYTD desc;

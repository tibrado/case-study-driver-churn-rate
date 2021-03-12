# case-study-driver-churn-rate

We started with making all of our columns non-string or meaningfully numeric. We got dummy variables for the city and Phone column. 


<details>

<summary> Data Dictionay </summary>

|#  |Column                | Count | Dtype | Definition|
|---|  ------              |-------|-------| ----------|
| 0 |  avg_dist            |    50000 | float64|The average distance (in miles) per trip taken in the first 30 days after signup|
| 1 |  avg_rating_by_driver|    50000 | float64|The rider’s average rating over all of their trips|
| 2 |  avg_rating_of_driver|    50000 | float64|The rider’s average rating of their drivers over all of their trips|
| 3 |  avg_surge           |    50000 | float64|The average surge multiplier over all of this user’s trips|
| 4 |  is_iphone           |    50000 | int64  |If driver use Iphone|
| 5 |  surge_pct           |    50000 | float64|The percent of trips taken with surge multiplier > 1|
| 6 |  trips_in_first_30_days|  50000 | int64  |The number of trips this user took in the first 30 days after signing up|
| 7 |  luxury_car_user       |  50000 |  int64  |1 if the user took a luxury car in their first 30 days; 0 otherwise|
| 8 |  weekday_pct           |  50000 |  float64|The percent of the user’s trips occurring during a weekday|
| 9 |  city_Astapor          |  50000 |  uint8  |City of Astapor|
| 10|  city_King's Landing   |  50000 |  uint8  |City of King's Landing
| 11|  city_Winterfell       |  50000 |  uint8  |City of Winterfell|
| 12|  last_trip_day         |  50000 |  int64  |Day of last trip|
| 13|  last_trip_month       |  50000 |  int64  |Month of last trip|
| 14|  signup_day            |  50000 |  int64  |Day of signup|
| 15|  signup_month          |  50000 |  int64 |Month of signup|
|16 | churn| 50000|uint8| 1 if driver churned|

</details>
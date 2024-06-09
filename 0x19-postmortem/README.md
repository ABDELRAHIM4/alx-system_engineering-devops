Issue Summary:
Duration: From 6:00 PM to 8:00 PM
Impact: 80% of users are affected.
Root Cause: Database overload due to inefficient query handling.

Timeline(all times pacific Time):
June 7th, 2024, 13:00 (UTC): Issue detected through monitoring alerts indicating increased response times.
June 7th, 2024, 13:15 (UTC): Engineering team initiated investigation, suspecting database-related issues.
June 7th, 2024, 14:30 (UTC): Initial investigation focused on application code, leading to misleading assumptions.
June 7th, 2024, 15:45 (UTC): Incident escalated to database administrators for further analysis.
June 8th, 2024, 07:00 (UTC): Root cause identified as database overload due to inefficient queries.
June 8th, 2024, 09:00 (UTC): Issue resolved by optimizing database queries and increasing server capacity.

Root Cause and Resolution:
The root cause of the outage was identified as inefficient database queries leading to database overload. Specifically, certain queries were not optimized, resulting in excessive resource consumption and degraded performance. To resolve the issue, database administrators optimized the problematic queries, implemented indexing where necessary, and increased server capacity to handle the load efficiently.

Corrective and Preventative Measures:
Improvements/Fixes:

-Implement regular code reviews to identify inefficient queries early in the development process.
-Enhance monitoring systems to detect performance degradation more accurately and proactively.
-Conduct periodic performance testing to identify potential bottlenecks before they impact users

Tasks to Address the Issue:
-Optimize all database queries to ensure efficient resource utilization.
-Implement automated alerts for abnormal database activity to facilitate early detection of similar issues.
-Review server capacity and scalability to accommodate future growth in user traffic.

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person as P
LEFT JOIN Address ON P.personId = A.personId;
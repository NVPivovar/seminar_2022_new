select
    user_id,
    name
from joom.external_user
where 1
    and login='$login'
    and password='$password';
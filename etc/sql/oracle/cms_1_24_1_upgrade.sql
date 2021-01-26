-- Running upgrade 50280c53117c -> 8ea9122275b1

CREATE INDEX "SUBSCRIPTIONS_STATE_IDX" ON subscriptions (state)

/

CREATE INDEX "CONTENTS_RULE_EVAL_FB_IDX" ON contents (rule_evaluation)

/

CREATE INDEX "REPLICAS_STATE_IDX" ON replicas (state)

/

CREATE INDEX "BAD_REPLICAS_ACCOUNT_IDX" ON bad_replicas (account)

/

CREATE INDEX "REQUESTS_DEST_RSE_ID_IDX" ON requests (dest_rse_id)

/

UPDATE alembic_version SET version_num='8ea9122275b1' WHERE alembic_version.version_num = '50280c53117c'

/

-- Running upgrade 8ea9122275b1 -> d23453595260

ALTER TABLE requests DROP CONSTRAINT "REQUESTS_STATE_CHK"

/

ALTER TABLE requests ADD CONSTRAINT "REQUESTS_STATE_CHK" CHECK (state in ('Q', 'G', 'S', 'D', 'F', 'L', 'N', 'O', 'A', 'U', 'W', 'M', 'P'))

/

UPDATE alembic_version SET version_num='d23453595260' WHERE alembic_version.version_num = '8ea9122275b1'


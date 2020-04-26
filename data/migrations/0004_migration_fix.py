from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20200426_1725'),
    ]

    migration = '''
        CREATE TRIGGER searchVectorUpdate BEFORE INSERT OR UPDATE
        ON data_video FOR EACH ROW EXECUTE PROCEDURE
        tsvector_update_trigger(searchVector, 'pg_catalog.english', title);

        -- Force triggers to run and populate the text_search column.
        UPDATE data_video set ID = ID;
    '''

    reverse_migration = '''
        DROP TRIGGER searchVectorUpdate ON data_video;
    '''

    operations = [
        migrations.RunSQL(migration, reverse_migration)
    ]
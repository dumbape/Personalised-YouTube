from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20200426_1849'),
    ]

    migration = '''
        CREATE TRIGGER searchVectorUpdate BEFORE INSERT OR UPDATE
        ON data_video FOR EACH ROW EXECUTE PROCEDURE
        tsvector_update_trigger(searchvector, 'pg_catalog.english', title, description);

        -- Force triggers to run and populate the text_search column.
    '''

    reverse_migration = '''
        DROP TRIGGER searchVectorUpdate ON data_video;
    '''

    operations = [
        migrations.RunSQL(migration, reverse_migration)
    ]
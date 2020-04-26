from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    migration = '''
        CREATE TRIGGER searchVectorUpdate BEFORE INSERT OR UPDATE
        ON data_video FOR EACH ROW EXECUTE FUNCTION
        tsvector_update_trigger(searchVector, 'pg_catalog.english', title);

        -- Force triggers to run and populate the text_search column.
        UPDATE data_video set ID = ID;
    '''

    reverse_migration = '''
        DROP TRIGGER searchVector ON data_video;
    '''

    operations = [
        migrations.RunSQL(migration, reverse_migration)
    ]

from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name') # 追加
            table.text('address') # 追加
            table.string('phone_number', 11) # 追加
            table.enum('sex', ['male', 'female']) # 追加
            table.timestamps()
            

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')

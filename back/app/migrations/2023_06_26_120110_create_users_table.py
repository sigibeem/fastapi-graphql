from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name') # 追加
            table.string('password') # 追加
            table.string('phonenumber', 11)
            table.text('address') # 追加
            table.enum('sex', ['male', 'female'])
            table.timestamps()
            

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')

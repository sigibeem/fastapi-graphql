from orator.migrations import Migration


class CreatePostsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('posts') as table:
            table.increments('id')
            table.integer('user_id').unsigned() # 追加
            table.foreign('user_id').references('id').on('users') # 追加
            table.string('todo') # 追加
            table.text('description') # 追加
            table.enum('status', ['Done', 'Doing', 'Ready', 'not Ready'])
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('posts')

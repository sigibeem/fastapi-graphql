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
            table.string('title') # 追加
            table.text('body') # 追加
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('posts')

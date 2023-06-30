from orator.migrations import Migration


class CreateCommentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('comments') as table:
            table.increments('id')
            table.integer('user_id').unsigned().nullable() # 追加
            table.foreign('user_id').references('id').on('users') # 追加
            table.integer('post_id').unsigned().nullable() # 追加
            table.foreign('post_id').references('id').on('posts') # 追加
            table.text('body') # 追加
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('comments')

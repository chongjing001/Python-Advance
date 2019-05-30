mysql添加外键.md

#### 
如果子表试图创建一个在父表中不存在的外键值，InnoDB会拒绝任何INSERT或UPDATE操作。如果父表试图UPDATE或者DELETE任何子表中存在或匹配的外键值，最终动作取决于外键约束定义中的ON UPDATE和ON DELETE选项。InnoDB支持5种不同的动作，如果没有指定ON DELETE或者ON UPDATE，默认的动作为RESTRICT:

1. CASCADE: 从父表中删除或更新对应的行，同时自动的删除或更新自表中匹配的行。ON DELETE CANSCADE和ON UPDATE CANSCADE都被InnoDB所支持。

2. SET NULL: 从父表中删除或更新对应的行，同时将子表中的外键列设为空。注意，这些在外键列没有被设为NOT NULL时才有效。ON DELETE SET NULL和ON UPDATE SET SET NULL都被InnoDB所支持。

3. NO ACTION: InnoDB拒绝删除或者更新父表。

4. RESTRICT: 拒绝删除或者更新父表。指定RESTRICT（或者NO ACTION）和忽略ON DELETE或者ON UPDATE选项的效果是一样的。

5. SET DEFAULT: InnoDB目前不支持。

外键约束使用最多的两种情况：

1）父表更新时子表也更新，父表删除时如果子表有匹配的项，删除失败；

2）父表更新时子表也更新，父表删除时子表匹配的项也删除。

前一种情况，在外键定义中，我们使用ON UPDATE CASCADE ON DELETE RESTRICT；
后一种情况，可以使用ON UPDATE CASCADE ON DELETE CASCAD

#### 添加外键 例：

- 1.创建表时直接创建外键约束
```sql
create table books(

    bookid number(10) not null primary key,

    bookName varchar2(20) not null,

    price number(10,2),

    categoryId number(10) not null references Category(id)  --外键约束

);
```
- 2.先创建表，表创建成功后，单独添加外键约束
**Alter table 表名 add constraint FK_ID foreign key(外键字段名) REFERENCES 外表表名(主键字段名)；**
```sql
create table books(

    bookid number(10) not null primary key,

    bookName varchar2(20) not null,

    price number(10,2),

    categoryId number(10) not null

);

ALTER TABLE  books ADD CONSTRAINT FK_Book_categoryid FOREIGN KEY(categoryId ) REFERENCES Category(id);
```


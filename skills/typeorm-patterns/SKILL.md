---
name: typeorm-patterns
description: TypeORM patterns and best practices for TypeScript/JavaScript. Entity design, relations, migrations, QueryBuilder, repositories, transactions. Use when working with TypeORM or designing database layers with decorators.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# TypeORM Patterns

> ORM for TypeScript and JavaScript. Supports MySQL, PostgreSQL, MariaDB, SQLite, MS SQL Server, Oracle.

## When to Use

- Setting up TypeORM in a project
- Designing entities and relations
- Writing migrations
- Using QueryBuilder for complex queries
- Choosing DataMapper vs ActiveRecord pattern
- Optimizing database queries

---

## Entity Design

### Basic Entity

```typescript
import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn } from "typeorm"

@Entity()
export class User {
  @PrimaryGeneratedColumn("uuid")
  id: string

  @Column({ unique: true })
  email: string

  @Column()
  firstName: string

  @Column()
  lastName: string

  @Column({ default: true })
  isActive: boolean

  @CreateDateColumn()
  createdAt: Date

  @UpdateDateColumn()
  updatedAt: Date
}
```

### Column Types

| Decorator | Use |
|-----------|-----|
| `@PrimaryGeneratedColumn()` | Auto-increment ID |
| `@PrimaryGeneratedColumn("uuid")` | UUID primary key |
| `@Column()` | Standard column |
| `@Column({ type: "text" })` | Text column |
| `@Column({ type: "json" })` | JSON column |
| `@Column({ nullable: true })` | Nullable column |
| `@Column({ default: 0 })` | Default value |
| `@Column({ select: false })` | Excluded from SELECT by default |
| `@CreateDateColumn()` | Auto-set on insert |
| `@UpdateDateColumn()` | Auto-set on update |
| `@DeleteDateColumn()` | Soft delete timestamp |

---

## Relations

### One-to-Many / Many-to-One

```typescript
@Entity()
export class User {
  @OneToMany(() => Post, (post) => post.author)
  posts: Post[]
}

@Entity()
export class Post {
  @ManyToOne(() => User, (user) => user.posts)
  author: User

  @Column()
  authorId: string  // Always expose FK column
}
```

### Many-to-Many

```typescript
@Entity()
export class Post {
  @ManyToMany(() => Tag, (tag) => tag.posts)
  @JoinTable()  // Only on ONE side
  tags: Tag[]
}

@Entity()
export class Tag {
  @ManyToMany(() => Post, (post) => post.tags)
  posts: Post[]
}
```

### One-to-One

```typescript
@Entity()
export class User {
  @OneToOne(() => Profile, (profile) => profile.user)
  profile: Profile
}

@Entity()
export class Profile {
  @OneToOne(() => User, (user) => user.profile)
  @JoinColumn()  // Only on ONE side
  user: User
}
```

### Relation Best Practices

| Rule | Why |
|------|-----|
| Always expose FK columns (`authorId`) | Avoids extra JOINs for simple reads |
| Use `eager: false` (default) | Prevents N+1 queries |
| Load relations explicitly | `relations: ["posts"]` in find options |
| Use `cascade` sparingly | Only when child can't exist without parent |

---

## DataMapper vs ActiveRecord

### DataMapper (Recommended)

```typescript
// Entities are plain objects, repositories handle persistence
const userRepo = dataSource.getRepository(User)
const user = userRepo.create({ email: "a@b.com", firstName: "Alex" })
await userRepo.save(user)
const found = await userRepo.findOneBy({ id: user.id })
```

### ActiveRecord

```typescript
// Entities extend BaseEntity, call methods on themselves
export class User extends BaseEntity { ... }

const user = User.create({ email: "a@b.com" })
await user.save()
const found = await User.findOneBy({ id: user.id })
```

| DataMapper | ActiveRecord |
|-----------|-------------|
| ✅ Better testability | ✅ Less boilerplate |
| ✅ Separation of concerns | ✅ Simpler for small projects |
| ✅ Preferred for large codebases | ❌ Tight coupling |

---

## QueryBuilder

### Basic Queries

```typescript
const users = await userRepo
  .createQueryBuilder("user")
  .where("user.isActive = :active", { active: true })
  .orderBy("user.createdAt", "DESC")
  .take(10)
  .skip(0)
  .getMany()
```

### Joins

```typescript
const posts = await postRepo
  .createQueryBuilder("post")
  .leftJoinAndSelect("post.author", "author")
  .leftJoinAndSelect("post.tags", "tag")
  .where("author.isActive = :active", { active: true })
  .getMany()
```

### Subqueries

```typescript
const qb = userRepo
  .createQueryBuilder("user")
  .where((qb) => {
    const subQuery = qb.subQuery()
      .select("post.authorId")
      .from(Post, "post")
      .where("post.likes > :likes")
      .getQuery()
    return "user.id IN " + subQuery
  })
  .setParameter("likes", 100)
```

---

## Migrations

### Commands

```bash
# Generate migration from entity changes
npx typeorm migration:generate -d src/data-source.ts src/migrations/AddUserTable

# Create empty migration
npx typeorm migration:create src/migrations/SeedData

# Run pending migrations
npx typeorm migration:run -d src/data-source.ts

# Revert last migration
npx typeorm migration:revert -d src/data-source.ts
```

### Migration Best Practices

| Rule | Why |
|------|-----|
| Never use `synchronize: true` in production | Causes data loss |
| Always review generated migrations | Auto-generation can be wrong |
| Make migrations reversible | Include proper `down()` |
| Test migrations on a copy of prod data | Catches edge cases |

---

## Transactions

```typescript
await dataSource.transaction(async (manager) => {
  const user = manager.create(User, { email: "a@b.com" })
  await manager.save(user)
  
  const profile = manager.create(Profile, { user })
  await manager.save(profile)
  // Both succeed or both fail
})
```

---

## Performance Tips

| Pattern | Impact |
|---------|--------|
| Use `select` to limit columns | Reduces data transfer |
| Use `loadRelationCountAndMap` | Count without loading |
| Add indices on WHERE/JOIN columns | Query speed |
| Use `take`/`skip` for pagination | Prevent full-table scans |
| Use `getRawMany()` for reports | Skip entity hydration |
| Cache with `cache: true` | Repeated queries |

---

## Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| `synchronize: true` in prod | Use migrations |
| Load all relations eagerly | Load only what you need |
| Raw SQL for simple queries | Use repository methods |
| Skip FK columns on entities | Always expose `authorId` etc. |
| Forget `@Index()` on query columns | Index WHERE/JOIN columns |
| Ignore connection pooling | Configure pool size for your env |

---

## Data Source Configuration

```typescript
import { DataSource } from "typeorm"

export const AppDataSource = new DataSource({
  type: "postgres",
  host: process.env.DB_HOST,
  port: parseInt(process.env.DB_PORT || "5432"),
  username: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: process.env.DB_NAME,
  synchronize: false, // NEVER true in production
  logging: process.env.NODE_ENV === "development",
  entities: ["src/entities/**/*.ts"],
  migrations: ["src/migrations/**/*.ts"],
  subscribers: ["src/subscribers/**/*.ts"],
})
```

---

> **Docs:** https://typeorm.io/
> **Source:** https://github.com/typeorm/typeorm

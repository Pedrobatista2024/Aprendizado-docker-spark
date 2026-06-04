create table produtos (
    id serial primary key,
    nome varchar(100),
    preco decimal(10, 2),
    estoque int
);

insert into produtos (nome, preco, estoque) values
('Produto A', 19.99, 100),
('Produto B', 29.99, 50),
('Produto C', 9.99, 200);

select * from public.produtos
where id = 1    ;
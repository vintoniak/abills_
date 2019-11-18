#!/usr/bin/perl

=head1 NAME

 Hello  world

=cut

use strict;
use warnings;

# Включение нужных путей
BEGIN {
  our $libpath = '../../';
  my $sql_type = 'mysql';
  unshift(@INC, $libpath . "Abills/$sql_type/", $libpath . "Abills/modules/", $libpath . '/lib/', $libpath . '/Abills/', $libpath);
}

#Модуль конфигурации
use Conf;
our ($libpath, %conf, %lang, $base_dir,);

# конфигурационный файл
do "../../libexec/config.pl";

# HTML визуализация
use Abills::HTML;
my $html = Abills::HTML->new(
  {
    IMG_PATH => 'img/',
    NO_PRINT => 1,
    CONF     => \%conf,
    CHARSET  => $conf{default_charset},
  }
);

# Подключение базы
use Abills::SQL;
my $db = Abills::SQL->connect(
  $conf{dbtype},
  $conf{dbhost},
  $conf{dbname},
  $conf{dbuser},
  $conf{dbpasswd},
  {
    CHARSET => ($conf{dbcharset}) ? $conf{dbcharset} : undef
  }
);

# Подключение модуля работы с шаблонами
require Abills::Templates;

$html->{METATAGS} = templates('metatags_client');

print $html->header();

# Диалоговое окно приветсвия
print $html->message('info', $lang{INFO}, "Hello world\nSystem name '$conf{WEB_TITLE}'");

1;


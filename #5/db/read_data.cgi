#!/usr/bin/perl
use strict;
use warnings;

use lib '/var/www/work/db_tpl';    # Add path of my module
use Main;                          # Add my module
use DBI;
use CGI;

my $Cgi = CGI->new;

print $Cgi->header("text/html");

# Add path to view files
my $tpl_main = TPL::load_tpl("view/main_tpl.tpl");
my $tpl_user = TPL::load_tpl("view/user_form.tpl");

# try to connect to database

my $dbh = DBI->connect("dbi:mysql:dbname=abills", "abills", "Vintoniak7______", { RaiseError => 1 },) or die $DBI::errstr;

# select DATA from mysql table

my $stm = $dbh->prepare("SELECT id, user_name, user_address, user_email FROM user_inform");
$stm->execute();

my $users_tpl;
while (my @user = $stm->fetchrow_array()) {
  my ($id, $user_name, $user_address, $user_email) = @user;

  $users_tpl .= TPL::render_tpl(
    $tpl_user,
    (
      USER_ID      => $id,
      USER_NAME    => $user_name,
      USER_ADDRESS => $user_address,
      USER_EMAIL   => $user_email
    )
  );
}

# calling a subroutine and to tpl real data ( changes the markers )
print TPL::render_tpl(
  $tpl_main,
  (
    TITLE   => "Users Panel",
    CONTENT => $users_tpl
  )
);

$stm->finish;
$dbh->disconnect;


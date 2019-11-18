#!/usr/bin/perl

use strict;
use warnings;
use IO::File;

package TPL;

#**********************************************************

=head2 load_tpl($path) - Load template
 
  Arguments:
    $path - Path for template file
 
  Returns:
    Text from file
 
  Example:
    load_tpl("home.tpl");
 
=cut

#**********************************************************
sub load_tpl {
  my ($path) = @_;
  my $tpl_file_text = "";

  my $Tpl_file = IO::File->new("<$path");

  while (<$Tpl_file>) {
    $tpl_file_text .= $_;
  }

  return $tpl_file_text;
}

#**********************************************************

=head2 render_tpl($path) - Load template
 
  Arguments:
    $tpl - text of template for parse
    %variables - hash with values for replays
 
  Returns:
    Parsed text
 
  Example:
    render_tpl($tpl, (title => "Home page"));
 
=cut

#**********************************************************
sub render_tpl {
  my ($tpl, %variables) = @_;

  my @names = keys %variables;

  while (<@names>) {
    $tpl =~ s/\%*$_*\%/$variables{$_}/g;
  }

  return $tpl;
}

1;

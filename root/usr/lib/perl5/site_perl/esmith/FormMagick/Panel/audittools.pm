#!/usr/bin/perl -w

package esmith::FormMagick::Panel::audittools;

use strict;
use warnings;
use esmith::FormMagick;
use esmith::cgi;
use esmith::util;
use CGI::Carp qw(fatalsToBrowser);


#use File::Basename;
#use Exporter;
#use Carp qw(verbose);
#use Getopt::Long;

our @ISA = qw(esmith::FormMagick Exporter);
our @EXPORT = qw(print_audittools);
 
sub print_audittools {
#my $param= shift;
    	my $self = shift;
    	my $q = $self->{cgi};

print $q->table ({border => 0, cellspacing => 0, cellpadding => 4},
    esmith::cgi::genTextRow ($q,
     $q->p ('Verify about groups and users :')));
    print $q->Tr (esmith::cgi::genButtonRow ($q,$q->submit (-name => 'state',-value => 'Verify Users and Groups')));     

#if (  $q->param ('state') eq "Verify Users and Groups")
       #{Scan_Local_Network ($q);}
        #{ foreach  (`/sbin/e-smith/audittools/groups-users`)
        #print $q->br($_);}
{my @a=`/sbin/e-smith/audittools/groups-users;/sbin/e-smith/audittools/newrpms`;

#my @a=`/sbin/e-smith/audittools/newrpms`;
 foreach my $b (@a)
{print $q->p($q->p ($b));}}
}
1;

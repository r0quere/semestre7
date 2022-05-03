


--*********************************************************************************
--		PILE GENERIQUE (un paramètre permet de déterminer la taille de la pile)
--*********************************************************************************
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

--/////////////////////
--    A COMPLETER


entity pile is
generic(taille_pile: integer:=4 ; taille_donnee:integer := 3);
port(
    calc, load, clk, raz_pile : in std_logic;
    d_in : in std_logic_vector(taille_donnee-1 downto 0);
    d_out : out std_logic_vector(taille_donnee-1 downto 0)
);
end pile;

architecture arch_pile  of pile is 
type type_pile is array(0 to taille_pile-1) of std_logic_vector(taille_donnee-1 downto 0);
signal tableau : type_pile;
begin
    process(clk, raz_pile)
begin
	if ( raz_pile='1')then
		for i in 0 to taille_pile-1 loop
			tableau(i)<= (others =>'0');
		end loop;
	
 	elsif rising_edge(clk) then
        	if (load='1') then 
			for i in 0 to taille_pile-2 loop
				tableau(taille_pile-1-i )<= tableau(taille_pile-2-i );
			end loop;
			tableau(0)<= d_in;
		
		elsif(calc='1') then
			for i in 0 to taille_pile-2 loop
				if (i=0) then 
				tableau(0)<= tableau(taille_pile-1);
				end if;
				tableau(i+1)<=tableau(i);
			end loop;
		end if;
	end if;
end process;

d_out<=tableau(taille_pile-1);

end arch_pile;

			





--/////////////////////


--*********************************************************************************
--		MULTIPLIEUR GENERIQUE
--*********************************************************************************
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;


--/////////////////////
--    A COMPLETER
entity multiplieur is
generic(taille_multiplieur: integer := 4);
port (
    E1,E2 : in std_logic_vector(taille_multiplieur-1 downto 0);
    S : out std_logic_vector(taille_multiplieur*2-1 downto 0)
);
end multiplieur;

architecture arch_multiplieur of multiplieur is
begin
	S<=std_logic_vector(signed(E1)*signed(E2));

end arch_multiplieur;


--/////////////////////



--*********************************************************************************
--		ADDITIONNEUR GENERIQUE
--*********************************************************************************
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

--/////////////////////
--    A COMPLETER

entity additionneur is
generic(taille_additionneur: integer := 8);
port (
    E1,E2 : in std_logic_vector(taille_additionneur-1 downto 0);
    S : out std_logic_vector(taille_additionneur-1 downto 0)
);
end additionneur;

architecture arch_additionneur of additionneur is
begin
	
	S<=std_logic_vector(signed(E1)+signed(E2));

end arch_additionneur;

--/////////////////////

--*********************************************************************************
--		REGISTRE GENERIQUE : taille de l'entrée et taille de la sortie paramétrables
--*********************************************************************************
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

--/////////////////////
--    A COMPLETER
--/////////////////////



--*********************************************************************************
--		SEQUENCEUR du CORRELATEUR
--*********************************************************************************
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

--/////////////////////
--    A COMPLETER
--/////////////////////

--*********************************************************************************
--		COMPTEUR DU SEQUENCEUR
--**********************************************************************
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

--/////////////////////
--    A COMPLETER
--/////////////////////


--*********************************************************************************
--*********************************************************************************
--	                              CORRELATEUR
--*********************************************************************************
--*********************************************************************************
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use work.stimul_pack.all;
use work.all;

--/////////////////////
--    A COMPLETER
--/////////////////////
   
      

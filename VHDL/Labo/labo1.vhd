library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity registre is
port ( reset,clk,load : in std_logic;
 Nb_place_max : in std_logic_vector ( 3 downto 0);
 D_out : out std_logic_vector(3 downto 0));
end registre;
architecture arch_register of registre is
begin
	process(clk,reset)
		begin
		if reset = '1' then D_out <= (others => '0');
		elsif rising_edge(clk) then
		  if load = '1' then D_out <= Nb_place_max;
		  end if;
		end if;
	end process;
end arch_register;

-- fin registre /////////////////////////////////////

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
 
entity compteur_base is
port
(   clk,reset,up,down   :   in std_logic;
    comptage       :   out std_logic_vector(3 downto 0));
end compteur_base;
 
architecture arch_compteur_base of compteur_base is
signal comptage_int : unsigned (3 downto 0);
begin
    process(clk,reset)
        begin
        if reset='1' then comptage_int <= (others => '0');
        elsif rising_edge(clk) then
            if up = '1' then comptage_int <= comptage_int + 1;
            elsif down = '1' then comptage_int <= comptage_int - 1;
            end if;
        end if;
    end process; 
comptage <= std_logic_vector(comptage_int); -- count copie de count_int 
end arch_compteur_base;

--fin compteur//////////////////////////////////////////////////////////////

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity detect_front_entre is 
port( clk,reset  :    in std_logic;
  E_entre       :    in std_logic;
  up : out std_logic);
end detect_front_entre;

architecture arch_detect_front_entre of detect_front_entre is
type etat_me is (E0,E1,E2);
signal etat_cr, etat_sv : etat_me;
begin

	process(clk,reset)        -- registre synchrone, maj etat_cr
        begin
        	if reset='1' then etat_cr <= E0;
                elsif rising_edge(clk) then etat_cr <= etat_sv;
                end if;
        end process;
   
   
	process(etat_cr,E_entre)        -- process combinatoire
        begin
	etat_sv <= etat_cr; up <= '0';

	case etat_cr is
		when E0 => if E_entre = '1' then etat_sv <= E1; end if;
		when E1 => etat_sv <= E2; up <= '1';
		when E2 => if E_entre = '0' then etat_sv <= E0; end if;
        end case;       
        end process;

end arch_detect_front_entre;
   
--fin detect front 1//////////////////////////////////////////////

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity detect_front_sortie is 
port( clk,reset  :    in std_logic;
  E_sortie       :    in std_logic;
  down : out std_logic);
end detect_front_sortie;

architecture arch_detect_front_sortie of detect_front_sortie is
type etat_me is (E0,E1,E2);
signal etat_cr, etat_sv : etat_me;
begin

	process(clk,reset)        -- registre synchrone, maj etat_cr
        begin
        	if reset='1' then etat_cr <= E0;
                elsif rising_edge(clk) then etat_cr <= etat_sv;
                end if;
        end process;
   
   
	process(etat_cr,E_sortie)        -- process combinatoire
        begin
	etat_sv <= etat_cr; down <= '0';

	case etat_cr is
		when E0 => if E_sortie = '1' then etat_sv <= E1; end if;
		when E1 => etat_sv <= E2; down <= '1';
		when E2 => if E_sortie = '0' then etat_sv <= E0; end if;
        end case;       
        end process;

end arch_detect_front_sortie;


--fin detect front 2//////////////////////////////////////////////

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all; -- types signed / unsigned (calcul)
 
entity soustracteur is
port(       comptage,D_out     :   in std_logic_vector(3 downto 0);
            Nb_places_dispos :   out std_logic_vector(3 downto 0));
end soustracteur;
 
architecture arch_soustracteur of soustracteur is
signal Nb_sous : unsigned(3 downto 0);
begin
    	Nb_sous <= unsigned (D_out) - unsigned ( comptage );
	Nb_places_dispos <= std_logic_vector(Nb_sous);
end arch_soustracteur;

--fin soustracteur ////////////////////////////////////////////////

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity comparateur is
port(        comptage,D_out  : in std_logic_vector(3 downto 0);
     Complet : out std_logic);
end comparateur; 

architecture arch_comparateur of comparateur is
begin

	Complet <= '0' when comptage >= D_out else '1';

end arch_comparateur;


--fin comparateur ///////////////////////////////


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use work.all;


entity parking is
port(reset, clk, load, E_entre,E_sortie: in std_logic;
	Complet : out std_logic );
end parking;

architecture arch_parking of parking is

signal up, down : std_logic;
signal cmp_value, reg_value,Nb_place_max, Nb_place_dispos  : std_logic_vector(3 downto 0);

begin
registres : entity registre port map ( reset => reset,
					clk => clk ,
					load => load ,
					Nb_place_max => Nb_place_max,
					D_out => reg_value );

compteur_bases : entity compteur_base port map ( clk => clk,
						 reset => reset,
						 up => up,
						 down => down,
						 comptage => cmp_value );

						
detect_front_entres : entity detect_front_entre port map ( clk => clk,
							 reset => reset,
							 E_entre => E_entre,
							  up => up );

detect_front_sorties : entity detect_front_sortie port map ( clk => clk,
							 reset => reset,
							 E_sortie => E_sortie,
							  down => down) ;

soustracteurs : entity soustracteur port map ( comptage => cmp_value,
					     D_out => reg_value ,
					     Nb_places_dispos => Nb_place_dispos );

comparateurs : entity comparateur port map (   comptage => cmp_value,
					     D_out => reg_value,
					     Complet => Complet );

end arch_parking;
 
--Mapping, appeler sa bibliotheque et definir, la plus grosse boite
